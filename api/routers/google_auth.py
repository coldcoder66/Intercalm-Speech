from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.requests import Request
from starlette.datastructures import Secret
from database import db_manager
from models import User
import os

# Handles Google OAuth2 authentication

# Load config from environment variables or .env file
config = Config(os.path.join(os.path.dirname(__file__), '..', '.env'))

router = APIRouter()
oauth = OAuth(config)

oauth.register(
    name='google',
    client_id=config.get('GOOGLE_CLIENT_ID'),
    client_secret=config.get('GOOGLE_CLIENT_SECRET', cast=Secret),
    server_metadata_url=config.get('GOOGLE_METADATA_URL', default='https://accounts.google.com/.well-known/openid-configuration'),
    client_kwargs={
        'scope': config.get('GOOGLE_CLIENT_SCOPE', default='openid email profile'),
    }
)

def get_current_user(request: Request):
    """Get current authenticated user from session"""
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    
    # Get user from database
    db = next(db_manager.get_db_session())
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    finally:
        db.close()

def require_auth(request: Request):
    """Dependency that requires authentication"""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user

@router.get('/login')
async def login(request: Request):
    """Initiate Google OAuth login"""
    # Store the original URL for redirect after login
    redirect_uri = request.url_for('auth_callback')
    request.session['login_redirect'] = request.query_params.get('redirect', '/')
    
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get('/callback')
async def auth_callback(request: Request):
    """Handle Google OAuth callback"""
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=f'Google login failed: {str(e)}')

    userinfo = token.get('userinfo')
    if not userinfo:
        raise HTTPException(status_code=400, detail='Failed to get user info from Google')

    # Get or create user in database
    user = db_manager.get_or_create_user(
        google_id=userinfo['sub'],
        email=userinfo['email'],
        name=userinfo['name'],
        picture=userinfo.get('picture')
    )
    
    if not user:
        raise HTTPException(status_code=500, detail='Failed to create or retrieve user')
    
    # Store user in session
    request.session['user_id'] = user.id
    request.session['user_email'] = user.email
    request.session['user_name'] = user.name
    
    # Redirect to original URL or home
    redirect_url = request.session.pop('login_redirect', '/')
    return RedirectResponse(url=redirect_url)

@router.get('/logout')
async def logout(request: Request):
    """Log out the current user"""
    # Clear session
    request.session.clear()
    
    return JSONResponse(
        content={"message": "Successfully logged out"},
        status_code=200
    )

@router.get('/profile')
async def get_profile(request: Request, user: User = Depends(require_auth)):
    """Get current user profile (protected route)"""
    return {
        "user": user.to_dict(),
        "authenticated": True
    }

@router.get('/status')
async def auth_status(request: Request):
    """Check authentication status"""
    user = get_current_user(request)
    
    if user:
        return {
            "authenticated": True,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "picture": user.picture
            }
        }
    else:
        return {
            "authenticated": False,
            "user": None
        }

@router.post('/logout')
async def logout_post(request: Request):
    """Alternative POST endpoint for logout (for forms)"""
    request.session.clear()
    return RedirectResponse(url='/', status_code=303)

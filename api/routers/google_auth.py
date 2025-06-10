from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.requests import Request
from starlette.datastructures import Secret
from database import db_manager
from models import User
import os
from jose import jwt, JWTError
from datetime import datetime, timedelta

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

# JWT settings
SECRET_KEY = config.get("JWT_SECRET_KEY") # Store this securely!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = config.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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
    """Handle Google OAuth callback and return JWT"""
    try:
        token_data = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return JSONResponse(
            status_code=400,
            content={'error': 'OAuth Error', 'error_description': error.description}
        )

    user_info = token_data.get('userinfo')
    if not user_info:
        # Try to parse id_token if userinfo is not directly available
        id_token_jwt = token_data.get('id_token')
        if id_token_jwt:
            try:
                # This decodes without verification, just to get claims for user lookup/creation
                # Verification should happen if you solely rely on id_token for auth decisions
                user_info = jwt.get_unverified_claims(id_token_jwt)
            except JWTError:
                return JSONResponse(
                    status_code=400,
                    content={'error': 'Invalid ID Token', 'error_description': 'Could not decode ID token.'}
                )
        else:
            return JSONResponse(
                status_code=400,
                content={'error': 'User Info Error', 'error_description': 'User info not found in token response.'}
            )

    google_id = user_info.get('sub') # 'sub' is standard for subject/user ID in OIDC
    email = user_info.get('email')
    name = user_info.get('name')
    picture = user_info.get('picture')

    if not google_id or not email:
        return JSONResponse(
            status_code=400,
            content={'error': 'User Info Error', 'error_description': 'Missing google_id or email in user info.'}
        )

    # Get or create user in your database
    db_user = db_manager.get_or_create_user(
        google_id=google_id,
        email=email,
        name=name,
        picture=picture
    )

    if not db_user:
        return JSONResponse(
            status_code=500,
            content={'error': 'Database Error', 'error_description': 'Could not get or create user.'}
        )

    # Create JWT
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(db_user.id), "email": db_user.email}, expires_delta=access_token_expires
    )

    return JSONResponse({"access_token": access_token, "token_type": "bearer"})

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

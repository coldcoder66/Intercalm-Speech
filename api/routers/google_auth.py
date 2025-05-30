from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.requests import Request
from starlette.datastructures import Secret
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
    server_metadata_url=config.get('GOOGLE_METADATA_URL'),
    client_kwargs={
        'scope': config.get('GOOGLE_CLIENT_SCOPE', default='openid email profile'),
    }
)

@router.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get('/callback')
async def auth_callback(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise HTTPException(status_code=400, detail='Google login failed')

    userinfo = token['userinfo']
    # Here you can create a session or JWT for the user
    return {"email": userinfo['email'], "name": userinfo['name']}

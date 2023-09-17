from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuthError

from app.OAuth import oauth

router = APIRouter()

@router.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.oauth.google.authorize_redirect(request, redirect_uri)


@router.route('/auth')
async def auth(request: Request):
    try:
        access_token = await oauth.oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    
    # user_data = await oauth.oauth.google.parse_id_token(request, access_token)
    # request.session['user'] = dict(user_data)
    user = access_token['userinfo']
    request.session['user'] = dict(user)
    return RedirectResponse(url='/')


@router.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')
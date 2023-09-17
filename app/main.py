from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.config import SECRET_KEY

app = FastAPI(title="ResQNet")

if SECRET_KEY is None:
    raise 'Missing SECRET_KEY'

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

from app.home import router as home_router
from app.auth import router as login_router

app.include_router(home_router.router, tags=["Home"])
app.include_router(login_router.router, tags=["Login"])
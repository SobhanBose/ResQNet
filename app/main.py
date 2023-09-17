from fastapi import FastAPI

app = FastAPI(title="ResQNet")

from app.home import router as home_router

app.include_router(home_router.router, tags=["Home"])
from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import router

app = FastAPI()

app.include_router(router.router)
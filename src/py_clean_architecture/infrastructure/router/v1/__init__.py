from fastapi import APIRouter

from .user import UserRouter

V1Router = APIRouter(prefix="/v1")
V1Router.include_router(router=UserRouter)

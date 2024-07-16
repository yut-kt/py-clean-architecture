from fastapi import APIRouter

from .v1 import V1Router

Router = APIRouter()
Router.include_router(V1Router)

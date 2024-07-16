from contextlib import asynccontextmanager

from fastapi import FastAPI

from .infrastructure import Router
from .infrastructure.database.setting import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):  # noqa: ANN201
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=Router)

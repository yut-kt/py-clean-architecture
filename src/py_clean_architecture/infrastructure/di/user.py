from fastapi import Depends

from py_clean_architecture.adapter import UserController, UserPresenterImpl
from py_clean_architecture.adapter.gateway.unit_of_work.user import UserUoWImpl
from py_clean_architecture.application import UserPresenter, UserUoW, UserUsecase
from py_clean_architecture.infrastructure import SessionLocal


def __di() -> UserController:
    uow: UserUoW = UserUoWImpl(SessionLocal)
    presenter: UserPresenter = UserPresenterImpl()
    usecase = UserUsecase(uow=uow, presenter=presenter)
    return UserController(usecase=usecase)


UserControllerDeps = Depends(__di)

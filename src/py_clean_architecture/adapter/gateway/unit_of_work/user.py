from sqlalchemy.orm import Session, sessionmaker

from py_clean_architecture.adapter.gateway.repository.account import AccountRepositoryImpl
from py_clean_architecture.adapter.gateway.repository.user import UserRepositoryImpl
from py_clean_architecture.application.unit_of_work.user import UserUoW
from py_clean_architecture.domain.service.user import UserService


class UserUoWImpl(UserUoW):
    user_service: UserService

    def __init__(self: "UserUoWImpl", session_factory: sessionmaker[Session]) -> None:
        super().__init__()
        self.__session_factory = session_factory

    def __enter__(self: "UserUoWImpl") -> "UserUoW":
        self.__session = self.__session_factory()
        self.__session.begin()
        user_repo = UserRepositoryImpl(self.__session)
        account_repo = AccountRepositoryImpl(self.__session)
        self.user_service = UserService(user_repo=user_repo, account_repo=account_repo)
        return self

    def __exit__(self: "UserUoWImpl", exc_type: type[BaseException] | None, *args: object) -> None:
        try:
            if exc_type is None:
                self.__session.commit()
            else:
                self.__session.rollback()
        finally:
            self.__session.close()

from abc import ABC

from py_clean_architecture.domain.service.user import UserService


class UserUoW(ABC):
    user_service: UserService

    def __enter__(self: "UserUoW") -> "UserUoW":
        raise NotImplementedError

    def __exit__(self: "UserUoW", *args: object) -> None:
        raise NotImplementedError

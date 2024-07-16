from abc import ABC, abstractmethod

from py_clean_architecture.domain import AccountRepository, UserEntity, UserRepository


class UserService(ABC):
    user_repo: UserRepository
    account_repo: AccountRepository

    @abstractmethod
    def create(self: "UserService", account_name: str) -> UserEntity:
        raise NotImplementedError

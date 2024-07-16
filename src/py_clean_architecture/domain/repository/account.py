from abc import ABC, abstractmethod

from py_clean_architecture.domain import AccountEntity


class AccountRepository(ABC):
    @abstractmethod
    def find_or_none(self: "AccountRepository", account_name: str) -> AccountEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create(self: "AccountRepository", user_id: int, account_name: str) -> AccountEntity:
        raise NotImplementedError

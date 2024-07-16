from abc import ABC, abstractmethod

from py_clean_architecture.domain import AccountEntity


class AccountRepository(ABC):
    @abstractmethod
    def create(self: "AccountRepository", user_id: int, account_name: str) -> AccountEntity:
        raise NotImplementedError

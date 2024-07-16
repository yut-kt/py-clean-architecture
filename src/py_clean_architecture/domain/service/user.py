from abc import ABC

from py_clean_architecture.domain import AccountRepository, DomainError, UserEntity, UserRepository


class UserService(ABC):
    user_repo: UserRepository
    account_repo: AccountRepository

    def __init__(self: "UserService", user_repo: UserRepository, account_repo: AccountRepository) -> None:
        self.user_repo = user_repo
        self.account_repo = account_repo

    def create(self: "UserService", account_name: str) -> UserEntity:
        if self.is_duplicate(account_name=account_name):
            msg = f"account name [{account_name}] is duplicated."
            raise DomainError(msg)
        user = self.user_repo.create()
        account = self.account_repo.create(user_id=user.identity, account_name=account_name)
        user.accounts.append(account)
        return user

    def is_duplicate(self: "UserService", account_name: str) -> bool:
        return bool(self.account_repo.find_or_none(account_name=account_name))

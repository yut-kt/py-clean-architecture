from py_clean_architecture.domain import AccountRepository, UserEntity, UserRepository
from py_clean_architecture.domain.service.user import UserService


class UserServiceImpl(UserService):
    def __init__(self, user_repo: UserRepository, account_repo: AccountRepository) -> None:
        self.user_repo = user_repo
        self.account_repo = account_repo

    def create(self: "UserServiceImpl", account_name: str) -> UserEntity:
        user = self.user_repo.create()
        account = self.account_repo.create(user_id=user.identity, account_name=account_name)
        user.accounts.append(account)
        return user

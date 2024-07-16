from py_clean_architecture.application import UserOutput, UserPresenter
from py_clean_architecture.domain import UserEntity


class UserPresenterImpl(UserPresenter):
    def created(self: "UserPresenterImpl", entity: UserEntity) -> UserOutput:
        accounts = entity.accounts
        return UserOutput(user_id=entity.identity, account_ids=[a.identity for a in accounts])

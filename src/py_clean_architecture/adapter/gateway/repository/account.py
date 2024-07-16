from sqlalchemy.orm import Session

from py_clean_architecture.domain import AccountEntity, AccountRepository
from py_clean_architecture.infrastructure import AccountModel


class AccountRepositoryImpl(AccountRepository):
    def __init__(self: "AccountRepositoryImpl", session: Session) -> None:
        self.session: Session = session

    def find_or_none(self: "AccountRepositoryImpl", account_name: str) -> AccountEntity | None:
        if model := self.session.query(AccountModel).filter(AccountModel.name == account_name).one_or_none():
            return AccountEntity(identity=model.identity, account_name=model.name)
        return None

    def create(self: "AccountRepositoryImpl", user_id: int, account_name: str) -> AccountEntity:
        model = AccountModel(user_id=user_id, name=account_name)
        self.session.add(model)
        self.session.flush()
        return AccountEntity(identity=model.identity)

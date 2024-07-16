from pydantic import BaseModel

from .account import AccountEntity


class UserEntity(BaseModel):
    identity: int
    accounts: list[AccountEntity]

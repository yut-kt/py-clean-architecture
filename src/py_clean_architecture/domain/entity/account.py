from pydantic import BaseModel


class AccountEntity(BaseModel):
    identity: int

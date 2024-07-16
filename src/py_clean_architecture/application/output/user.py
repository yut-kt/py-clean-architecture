from pydantic import BaseModel


class UserOutput(BaseModel):
    user_id: int
    account_ids: list[int]

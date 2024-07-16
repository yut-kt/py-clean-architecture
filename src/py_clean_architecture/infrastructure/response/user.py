from pydantic import BaseModel


class UserCreateResponse(BaseModel):
    user_id: int
    account_ids: list[int]

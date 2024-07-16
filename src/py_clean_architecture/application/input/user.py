from pydantic import BaseModel


class UserInput(BaseModel):
    account_name: str

from pydantic import BaseModel, constr


class UserCreateRequest(BaseModel):
    account_name: constr(min_length=1, max_length=16, to_lower=True, strip_whitespace=True)

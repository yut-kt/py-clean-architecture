from fastapi import APIRouter
from starlette import status

from py_clean_architecture.adapter import UserController
from py_clean_architecture.infrastructure import UserControllerDeps, UserCreateRequest, UserCreateResponse

UserRouter = APIRouter(prefix="/users")


@UserRouter.post(
    "",
    response_model=UserCreateResponse,
    status_code=status.HTTP_201_CREATED,
    description="User create endpoint",
    tags=["user"],
)
def create(req_model: UserCreateRequest, controller: UserController = UserControllerDeps) -> UserCreateResponse:
    user_id, account_ids = controller.create(account_name=req_model.account_name)
    return UserCreateResponse(user_id=user_id, account_ids=account_ids)

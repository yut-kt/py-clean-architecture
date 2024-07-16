from py_clean_architecture.application import UserInput, UserUsecase


class UserController:
    def __init__(self: "UserController", usecase: UserUsecase) -> None:
        self.usecase = usecase

    def create(self: "UserController", account_name: str) -> (str, list[str]):
        output = self.usecase.create(UserInput(account_name=account_name))
        return output.user_id, output.account_ids

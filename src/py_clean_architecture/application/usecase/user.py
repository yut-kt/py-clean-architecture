from py_clean_architecture.application import UserInput, UserOutput, UserPresenter, UserUoW


class UserUsecase:
    def __init__(self: "UserUsecase", uow: UserUoW, presenter: UserPresenter) -> None:
        self.uow = uow
        self.presenter = presenter

    def create(self: "UserUsecase", i: UserInput) -> UserOutput:
        with self.uow as uow:
            user = uow.user_service.create(account_name=i.account_name)
            return self.presenter.created(user)

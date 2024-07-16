import logging

from sqlalchemy.orm import Session

from py_clean_architecture.domain import UserEntity, UserRepository
from py_clean_architecture.infrastructure import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self: "UserRepositoryImpl", session: Session) -> None:
        self.session: Session = session

    def create(self: "UserRepositoryImpl") -> UserEntity:
        model = UserModel()
        self.session.add(model)
        self.session.flush()
        return UserEntity(identity=model.identity, accounts=[])

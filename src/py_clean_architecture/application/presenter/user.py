from abc import ABC, abstractmethod

from py_clean_architecture.application import UserOutput
from py_clean_architecture.domain import UserEntity


class UserPresenter(ABC):
    @abstractmethod
    def created(self: "UserPresenter", entity: UserEntity) -> UserOutput:
        raise NotImplementedError

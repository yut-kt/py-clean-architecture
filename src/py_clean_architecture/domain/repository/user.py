from abc import ABC, abstractmethod

from py_clean_architecture.domain import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def create(self: "UserRepository") -> UserEntity:
        raise NotImplementedError

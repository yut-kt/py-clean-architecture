from typing import TYPE_CHECKING

from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from .account import AccountModel


class UserModel(Base):
    __tablename__ = "user"

    identity: Mapped[int] = mapped_column(
        INTEGER(10, unsigned=True, zerofill=True),
        primary_key=True,
        autoincrement=True,
    )
    accounts: Mapped[list["AccountModel"]] = relationship(back_populates="user")

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from .user import UserModel


class AccountModel(Base):
    __tablename__ = "account"

    identity: Mapped[int] = mapped_column(
        INTEGER(10, unsigned=True, zerofill=True),
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("user.identity"))
    name: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    user: Mapped["UserModel"] = relationship(back_populates="accounts")

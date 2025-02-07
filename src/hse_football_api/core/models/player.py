from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Player(Base, IdPkMixin):
    __tablename__ = "players"

    name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    date_of_birth: Mapped[datetime]
    is_verified: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"<Player(id={self.id}, name={self.name} {self.last_name})>"

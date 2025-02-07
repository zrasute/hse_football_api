from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Team(Base, IdPkMixin):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(32))

    def __repr__(self) -> str:
        return f"<Team(id={self.id}, name={self.name})>"

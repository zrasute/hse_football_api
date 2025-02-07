from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Tournament(Base, IdPkMixin):
    __tablename__ = "tournaments"

    name: Mapped[str] = mapped_column(String(32))
    level: Mapped[str] = mapped_column(String(32))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    is_league: Mapped[bool]

    def __repr__(self) -> str:
        return f"<Tournament(id={self.id}, name={self.name})>"

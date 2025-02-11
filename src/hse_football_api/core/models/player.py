from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .match_event import MatchEvent
    from .player_statistics import PlayerStatistics
    from .roster import Roster


class Player(Base, IdPkMixin):
    __tablename__ = "players"

    name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    date_of_birth: Mapped[datetime]
    is_verified: Mapped[bool] = mapped_column(default=False)

    rosters: Mapped[list["Roster"]] = relationship(
        back_populates="player",
        cascade="all, delete-orphan",
    )
    statistics: Mapped[list["PlayerStatistics"]] = relationship(
        back_populates="player",
        cascade="all, delete-orphan",
    )
    match_events: Mapped[list["MatchEvent"]] = relationship(
        back_populates="player",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Player(id={self.id}, name={self.name} {self.last_name})>"

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .match import Match
    from .player_statistics import PlayerStatistics
    from .roster import Roster
    from .tournament_standings import TournamentStandings


class Tournament(Base, IdPkMixin):
    __tablename__ = "tournaments"

    name: Mapped[str] = mapped_column(String(32))
    level: Mapped[str] = mapped_column(String(32))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    is_league: Mapped[bool]

    rosters: Mapped[list["Roster"]] = relationship(back_populates="tournament")
    player_statistics: Mapped[list["PlayerStatistics"]] = relationship(
        back_populates="tournament",
        cascade="all, delete-orphan",
    )
    matches: Mapped[list["Match"]] = relationship(back_populates="tournament")
    standings: Mapped[list["TournamentStandings"]] = relationship(
        back_populates="tournament"
    )

    def __repr__(self) -> str:
        return f"<Tournament(id={self.id}, name={self.name})>"

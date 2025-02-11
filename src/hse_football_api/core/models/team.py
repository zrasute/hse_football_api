from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .manager import Manager
    from .match import Match
    from .match_event import MatchEvent
    from .roster import Roster
    from .tournament_standings import TournamentStandings


class Team(Base, IdPkMixin):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(32))

    rosters: Mapped[list["Roster"]] = relationship(back_populates="team")
    match_events: Mapped[list["MatchEvent"]] = relationship(back_populates="team")
    standings: Mapped[list["TournamentStandings"]] = relationship(back_populates="team")
    managers: Mapped[list["Manager"]] = relationship(back_populates="team")
    home_matches: Mapped[list["Match"]] = relationship(
        back_populates="home_team",
        foreign_keys="matches.home_team_id",
    )
    away_matches: Mapped[list["Match"]] = relationship(
        back_populates="away_team",
        foreign_keys="matches.away_team_id",
    )

    def __repr__(self) -> str:
        return f"<Team(id={self.id}, name={self.name})>"

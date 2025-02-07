import uuid

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TournamentStandings(Base):
    __tablename__ = "tournament_standings"

    tournament_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tournaments.id"),
        primary_key=True,
    )
    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("teams.id"),
        primary_key=True,
    )
    matches_played: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    wins: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    draws: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    losses: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    goals_scored: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    goals_missed: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    goal_diff: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    points: Mapped[int] = mapped_column(default=0, server_default=text("0"))

    def __repr__(self) -> str:
        return (
            f"<TournamentStandings(tournament_id={self.tournament_id}, "
            f"team_id={self.team_id})>"
        )

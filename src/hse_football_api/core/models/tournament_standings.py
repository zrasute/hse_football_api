import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .team import Team
    from .tournament import Tournament


class TournamentStandings(Base):
    """
    Association object representing a many-to-many relationship
    between Player and Tournament.

    This table tracks teams statistics for a specific tournament.
    """

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

    tournament: Mapped["Tournament"] = relationship(back_populates="standings")
    team: Mapped["Team"] = relationship(back_populates="standings")

    def __repr__(self) -> str:
        return (
            f"<TournamentStandings(tournament_id={self.tournament_id}, "
            f"team_id={self.team_id})>"
        )

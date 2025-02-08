import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player
    from .team import Team
    from .tournament import Tournament


class Roster(Base):
    """
    Association object representing a many-to-many relationship
    between Player, Team, and Tournament.

    This table tracks which players are included in a team's roster
    for a specific tournament. It also stores additional attributes
    such as the date a player joined and (optionally) left the roster.
    """

    __tablename__ = "rosters"

    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id"),
        primary_key=True,
    )
    team_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("teams.id"),
        primary_key=True,
    )
    tournament_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tournaments.id"),
        primary_key=True,
    )
    joined_at: Mapped[datetime]
    left_at: Mapped[datetime | None]

    player: Mapped["Player"] = relationship(back_populates="rosters")
    tournament: Mapped["Tournament"] = relationship(back_populates="rosters")
    team: Mapped["Team"] = relationship(back_populates="rosters")

    def __repr__(self) -> str:
        return (
            f"<Roster(player_id={self.player_id}, "
            f"team_id={self.team_id}, "
            f"tournament_id={self.tournament_id})>"
        )

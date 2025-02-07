import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Roster(Base):
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

    def __repr__(self) -> str:
        return (
            f"<Roster(player_id={self.player_id}, "
            f"team_id={self.team_id}, "
            f"tournament_id={self.tournament_id})>"
        )

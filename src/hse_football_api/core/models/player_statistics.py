import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player
    from .tournament import Tournament


class PlayerStatistics(Base):
    """
    Association object representing a many-to-many relationship
    between Player and Tournament.

    This table tracks player statistics for a specific tournament.
    """

    __tablename__ = "player_statistics"

    player_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("players.id"),
        primary_key=True,
    )
    tournament_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tournaments.id"),
        primary_key=True,
    )
    matches_played: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    goals: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    assists: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    yellow_cards: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    red_cards: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    minutes_played: Mapped[int] = mapped_column(default=0, server_default=text("0"))

    player: Mapped["Player"] = relationship(back_populates="statistics")
    tournament: Mapped["Tournament"] = relationship(back_populates="player_statistics")

    def __repr__(self) -> str:
        return (
            f"<PlayerStatistics(player_id={self.player_id}, "
            f"tournament_id={self.tournament_id})>"
        )

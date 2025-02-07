import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Match(Base, IdPkMixin):
    __tablename__ = "matches"

    __table_args__ = (
        CheckConstraint(
            "referee_rating >= 0 AND referee_rating <= 5", name="referee_rating"
        ),
    )

    tournament_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tournaments.id"))
    home_team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    away_team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    score_home_team: Mapped[int] = mapped_column(default=0)
    score_away_team: Mapped[int] = mapped_column(default=0)
    date: Mapped[datetime]
    referee_rating: Mapped[int]
    stage: Mapped[str] = mapped_column(String(32))

    def __repr__(self) -> str:
        return (
            f"<Match(id={self.id}, "
            f"home_team_id={self.home_team_id}, "
            f"away_team_id={self.away_team_id})>"
        )

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .match_event import MatchEvent
    from .team import Team
    from .tournament import Tournament


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

    events: Mapped[list["MatchEvent"]] = relationship(
        back_populates="match",
        cascade="all, delete-orphan",
    )
    tournament: Mapped["Tournament"] = relationship(back_populates="matches")
    home_team: Mapped["Team"] = relationship(
        back_populates="home_matches",
        foreign_keys=home_team_id,
    )
    away_team: Mapped["Team"] = relationship(
        back_populates="away_matches",
        foreign_keys=away_team_id,
    )

    def __repr__(self) -> str:
        return (
            f"<Match(id={self.id}, "
            f"home_team_id={self.home_team_id}, "
            f"away_team_id={self.away_team_id})>"
        )

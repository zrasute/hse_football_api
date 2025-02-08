from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .match_event import MatchEvent
    from .roster import Roster


class Team(Base, IdPkMixin):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(32))

    rosters: Mapped[list["Roster"]] = relationship(back_populates="team")
    match_events: Mapped[list["MatchEvent"]] = relationship(back_populates="team")

    def __repr__(self) -> str:
        return f"<Team(id={self.id}, name={self.name})>"

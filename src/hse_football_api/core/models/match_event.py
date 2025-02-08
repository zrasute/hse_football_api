import uuid

from sqlalchemy import CheckConstraint, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .enums import EventType
from .mixins import IdPkMixin


class MatchEvent(Base, IdPkMixin):
    __tablename__ = "match_events"

    __table_args__ = (
        CheckConstraint("event_time >= 0 AND event_time <= 60", name="event_time"),
    )

    match_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("matches.id"))
    team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    player_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("players.id"))
    event_type: Mapped[EventType] = mapped_column(
        Enum(EventType, name="event_type_enum")
    )
    event_time: Mapped[int]

    def __repr__(self) -> str:
        return (
            f"<MatchEvent(id={self.id}, "
            f"match_id={self.match_id}, "
            f"event_type={self.event_type.value})>"
        )

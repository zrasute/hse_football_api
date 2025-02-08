import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .team import Team


class Manager(Base, IdPkMixin):
    __tablename__ = "managers"

    __table_args__ = (UniqueConstraint("team_id", "manager_id"),)

    team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    manager_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("players.id"))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime | None]

    team: Mapped["Team"] = relationship(back_populates="managers")

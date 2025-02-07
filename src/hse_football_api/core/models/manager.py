import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Manager(Base, IdPkMixin):
    __tablename__ = "managers"

    __table_args__ = (UniqueConstraint("team_id", "manager_id"),)

    team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    manager_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("players.id"))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime | None]

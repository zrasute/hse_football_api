from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from hse_football_api.core.config import settings


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=settings.db.naming_convention)

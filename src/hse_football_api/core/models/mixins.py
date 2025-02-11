import uuid

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class IdPkMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )

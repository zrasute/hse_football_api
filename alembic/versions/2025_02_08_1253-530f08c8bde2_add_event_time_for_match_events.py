"""add event_time for match_events

Revision ID: 530f08c8bde2
Revises: 8eca0c477644
Create Date: 2025-02-08 12:53:08.172141

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "530f08c8bde2"
down_revision: Union[str, None] = "8eca0c477644"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("match_events", sa.Column("event_time", sa.Integer(), nullable=False))
    op.create_check_constraint(
        op.f("ck_match_events_event_time"),
        "match_events",
        "event_time >= 0 AND event_time <= 60",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("ck_match_events_event_time"),
        "match_events",
        type_="check",
    )
    op.drop_column("match_events", "event_time")

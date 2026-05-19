"""create teams table

Revision ID: 4affb479966b
Revises: 58de2a51706a
Create Date: 2025-02-07 14:04:13.326521

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4affb479966b"
down_revision: str | None = "58de2a51706a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "teams",
        sa.Column(
            "id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_teams")),
    )


def downgrade() -> None:
    op.drop_table("teams")

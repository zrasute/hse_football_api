"""create players table

Revision ID: 58de2a51706a
Revises:
Create Date: 2025-02-07 13:30:25.061041

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "58de2a51706a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "players",
        sa.Column(
            "id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("last_name", sa.String(length=32), nullable=False),
        sa.Column("date_of_birth", sa.DateTime(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_players")),
    )


def downgrade() -> None:
    op.drop_table("players")

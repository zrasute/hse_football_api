"""create managers table

Revision ID: 8eca0c477644
Revises: 3596aa61fbf2
Create Date: 2025-02-07 18:33:32.611642

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8eca0c477644"
down_revision: Union[str, None] = "3596aa61fbf2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "managers",
        sa.Column(
            "id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column("manager_id", sa.Uuid(), nullable=False),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["manager_id"], ["players.id"], name=op.f("fk_managers_manager_id_players")
        ),
        sa.ForeignKeyConstraint(
            ["team_id"], ["teams.id"], name=op.f("fk_managers_team_id_teams")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_managers")),
        sa.UniqueConstraint(
            "team_id", "manager_id", name=op.f("uq_managers_team_id_manager_id")
        ),
    )


def downgrade() -> None:
    op.drop_table("managers")

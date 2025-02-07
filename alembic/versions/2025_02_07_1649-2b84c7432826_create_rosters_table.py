"""create rosters table

Revision ID: 2b84c7432826
Revises: 4494bfc197ea
Create Date: 2025-02-07 16:49:08.871697

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2b84c7432826"
down_revision: Union[str, None] = "4494bfc197ea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "rosters",
        sa.Column("player_id", sa.Uuid(), nullable=False),
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column("tournament_id", sa.Uuid(), nullable=False),
        sa.Column("joined_at", sa.DateTime(), nullable=False),
        sa.Column("left_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["player_id"], ["players.id"], name=op.f("fk_rosters_player_id_players")
        ),
        sa.ForeignKeyConstraint(
            ["team_id"], ["teams.id"], name=op.f("fk_rosters_team_id_teams")
        ),
        sa.ForeignKeyConstraint(
            ["tournament_id"],
            ["tournaments.id"],
            name=op.f("fk_rosters_tournament_id_tournaments"),
        ),
        sa.PrimaryKeyConstraint(
            "player_id", "team_id", "tournament_id", name=op.f("pk_rosters")
        ),
    )


def downgrade() -> None:
    op.drop_table("rosters")

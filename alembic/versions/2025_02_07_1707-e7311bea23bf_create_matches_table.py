"""create matches table

Revision ID: e7311bea23bf
Revises: 2b84c7432826
Create Date: 2025-02-07 17:07:33.429523

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e7311bea23bf"
down_revision: Union[str, None] = "2b84c7432826"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "matches",
        sa.Column(
            "id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("tournament_id", sa.Uuid(), nullable=False),
        sa.Column("home_team_id", sa.Uuid(), nullable=False),
        sa.Column("away_team_id", sa.Uuid(), nullable=False),
        sa.Column("score_home_team", sa.Integer(), nullable=False),
        sa.Column("score_away_team", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("referee_rating", sa.Integer(), nullable=False),
        sa.Column("stage", sa.String(length=32), nullable=False),
        sa.CheckConstraint(
            "referee_rating >= 0 AND referee_rating <= 5",
            name=op.f("ck_matches_referee_rating"),
        ),
        sa.ForeignKeyConstraint(
            ["away_team_id"], ["teams.id"], name=op.f("fk_matches_away_team_id_teams")
        ),
        sa.ForeignKeyConstraint(
            ["home_team_id"], ["teams.id"], name=op.f("fk_matches_home_team_id_teams")
        ),
        sa.ForeignKeyConstraint(
            ["tournament_id"],
            ["tournaments.id"],
            name=op.f("fk_matches_tournament_id_tournaments"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_matches")),
    )


def downgrade() -> None:
    op.drop_table("matches")

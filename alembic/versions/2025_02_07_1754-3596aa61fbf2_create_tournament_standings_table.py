"""create tournament_standings table

Revision ID: 3596aa61fbf2
Revises: 8f2224ad521e
Create Date: 2025-02-07 17:54:56.414057

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3596aa61fbf2"
down_revision: Union[str, None] = "8f2224ad521e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tournament_standings",
        sa.Column("tournament_id", sa.Uuid(), nullable=False),
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column(
            "matches_played", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column("wins", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("draws", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("losses", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column(
            "goals_scored", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column(
            "goals_missed", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column(
            "goal_diff", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column("points", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["teams.id"],
            name=op.f("fk_tournament_standings_team_id_teams"),
        ),
        sa.ForeignKeyConstraint(
            ["tournament_id"],
            ["tournaments.id"],
            name=op.f("fk_tournament_standings_tournament_id_tournaments"),
        ),
        sa.PrimaryKeyConstraint(
            "tournament_id", "team_id", name=op.f("pk_tournament_standings")
        ),
    )


def downgrade() -> None:
    op.drop_table("tournament_standings")

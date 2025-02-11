"""create player_statistics table

Revision ID: 4494bfc197ea
Revises: 2f7a2dd365f7
Create Date: 2025-02-07 14:35:40.086025

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4494bfc197ea"
down_revision: Union[str, None] = "2f7a2dd365f7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "player_statistics",
        sa.Column("player_id", sa.Uuid(), nullable=False),
        sa.Column("tournament_id", sa.Uuid(), nullable=False),
        sa.Column(
            "matches_played", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column("goals", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("assists", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column(
            "yellow_cards", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column(
            "red_cards", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.Column(
            "minutes_played", sa.Integer(), server_default=sa.text("0"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
            name=op.f("fk_player_statistics_player_id_players"),
        ),
        sa.ForeignKeyConstraint(
            ["tournament_id"],
            ["tournaments.id"],
            name=op.f("fk_player_statistics_tournament_id_tournaments"),
        ),
        sa.PrimaryKeyConstraint(
            "player_id", "tournament_id", name=op.f("pk_player_statistics")
        ),
    )


def downgrade() -> None:
    op.drop_table("player_statistics")

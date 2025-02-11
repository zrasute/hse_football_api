"""create match_events table

Revision ID: 8f2224ad521e
Revises: e7311bea23bf
Create Date: 2025-02-07 17:28:11.624811

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8f2224ad521e"
down_revision: Union[str, None] = "e7311bea23bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "match_events",
        sa.Column(
            "id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("match_id", sa.Uuid(), nullable=False),
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column("player_id", sa.Uuid(), nullable=False),
        sa.Column(
            "event_type",
            sa.Enum(
                "goal", "assist", "yellow_card", "red_card", name="event_type_enum"
            ),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["match_id"], ["matches.id"], name=op.f("fk_match_events_match_id_matches")
        ),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
            name=op.f("fk_match_events_player_id_players"),
        ),
        sa.ForeignKeyConstraint(
            ["team_id"], ["teams.id"], name=op.f("fk_match_events_team_id_teams")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_match_events")),
    )


def downgrade() -> None:
    op.drop_table("match_events")

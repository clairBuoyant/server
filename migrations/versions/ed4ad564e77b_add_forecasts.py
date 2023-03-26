""" Add Forecasts

Revision ID: 0d4ad564e77b
Revises: d63493af0a71
Create Date: 2023-03-26 12:46:10.999340

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0d4ad564e77b"
down_revision = "d63493af0a71"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "forecasts",
        sa.Column("id", sa.Integer(), nullable=False, unique=True),
        sa.Column("date_recorded", sa.DateTime(), nullable=False),
        sa.Column("station_id", sa.String(length=10), nullable=False),
        sa.Column("wave_height", sa.Float(), nullable=True),
        sa.Column("wind_direction", sa.Integer(), nullable=True),
        sa.Column("wind_speed", sa.Float(), nullable=True),
        sa.Column("wind_speed_gust", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(
            ["station_id"],
            ["buoys.station_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_forecasts_id"), "forecasts", ["id"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_forecasts_id"), table_name="forecasts")
    op.drop_table("forecasts")

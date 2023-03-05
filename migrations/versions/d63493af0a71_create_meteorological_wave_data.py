"""Create meteorological and wave data tables.

Revision ID: d63493af0a71
Revises: 6fc1a99cefd5
Create Date: 2022-08-20 14:01:00.212730

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d63493af0a71"
down_revision = "6fc1a99cefd5"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "meteorological_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("station_id", sa.String(length=10), nullable=False),
        sa.Column("date_recorded", sa.DateTime(), nullable=False),
        sa.Column("wind_direction", sa.Integer(), nullable=True),
        sa.Column("wind_speed", sa.Float(), nullable=True),
        sa.Column("wind_gust", sa.Float(), nullable=True),
        sa.Column("wave_height", sa.Float(), nullable=True),
        sa.Column("dominant_wave_period", sa.Float(), nullable=True),
        sa.Column("average_wave_period", sa.Float(), nullable=True),
        sa.Column("wave_direction", sa.Integer(), nullable=True),
        sa.Column("sea_level_pressure", sa.Float(), nullable=True),
        sa.Column("pressure_tendency", sa.Float(), nullable=True),
        sa.Column("air_temperature", sa.Float(), nullable=True),
        sa.Column("water_temperature", sa.Float(), nullable=True),
        sa.Column("dewpoint_temperature", sa.Float(), nullable=True),
        sa.Column("visibility", sa.Float(), nullable=True),
        sa.Column("tide", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(
            ["station_id"],
            ["buoys.station_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_meteorological_data_id"), "meteorological_data", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_meteorological_data_station_id"),
        "meteorological_data",
        ["station_id"],
        unique=False,
    )
    op.create_table(
        "wave_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("station_id", sa.String(length=10), nullable=False),
        sa.Column("date_recorded", sa.DateTime(), nullable=False),
        sa.Column("significant_wave_height", sa.Float(), nullable=True),
        sa.Column("swell_height", sa.Float(), nullable=True),
        sa.Column("swell_period", sa.Float(), nullable=True),
        sa.Column("wind_wave_height", sa.Float(), nullable=True),
        sa.Column("wind_wave_period", sa.Float(), nullable=True),
        sa.Column("swell_direction", sa.String(), nullable=True),
        sa.Column("wind_wave_direction", sa.String(), nullable=True),
        sa.Column("steepness", sa.String(), nullable=True),
        sa.Column("average_wave_period", sa.Float(), nullable=True),
        sa.Column("mean_wave_direction", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["station_id"],
            ["buoys.station_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_wave_data_id"), "wave_data", ["id"], unique=False)
    op.create_index(
        op.f("ix_wave_data_station_id"), "wave_data", ["station_id"], unique=False
    )


def downgrade():
    op.drop_index(op.f("ix_wave_data_station_id"), table_name="wave_data")
    op.drop_index(op.f("ix_wave_data_id"), table_name="wave_data")
    op.drop_table("wave_data")
    op.drop_index(
        op.f("ix_meteorological_data_station_id"), table_name="meteorological_data"
    )
    op.drop_index(op.f("ix_meteorological_data_id"), table_name="meteorological_data")
    op.drop_table("meteorological_data")

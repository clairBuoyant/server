"""create buoys

Revision ID: d632ea3490c4
Revises:
Create Date: 2021-12-25 20:31:21.052080

"""
from alembic import op
from geoalchemy2.types import Geography
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "d632ea3490c4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "buoys",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("station_id", sa.String(length=10), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("owner", sa.String(length=200), nullable=False),
        sa.Column(
            "location",
            Geography(
                geometry_type="POINT",
                srid=4326,
                from_text="ST_GeogFromText",
                name="geography",
            ),
            nullable=False,
        ),
        sa.Column("elev", sa.Float(precision=10), nullable=False),
        sa.Column("pgm", sa.String(length=50), nullable=False),
        sa.Column("type", sa.String(length=10), nullable=False),
        sa.Column("met", sa.String(length=1), nullable=False),
        sa.Column("currents", sa.String(length=1), nullable=False),
        sa.Column("water_quality", sa.String(length=1), nullable=False),
        sa.Column("dart", sa.String(length=1), nullable=False),
        sa.Column("seq", sa.SmallInteger(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_buoys_id"), "buoys", ["id"], unique=False)
    op.create_index(op.f("ix_buoys_station_id"), "buoys", ["station_id"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_buoys_station_id"), table_name="buoys")
    op.drop_index(op.f("ix_buoys_id"), table_name="buoys")
    op.drop_table("buoys")

"""create buoys

Revision ID: d632ea3490c4
Revises:
Create Date: 2021-12-25 20:31:21.052080

"""
import sqlalchemy as sa
from alembic import op
from geoalchemy2.types import Geography  # type: ignore

# revision identifiers, used by Alembic.
revision = "d632ea3490c4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "buoys",
        sa.Column(
            "id",
            sa.Integer(),
            index=True,
            nullable=False,
            primary_key=True,
            unique=True,
        ),
        sa.Column(
            "station_id",
            sa.String(length=10),
            index=True,
            nullable=False,
            unique=True,
        ),
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
    )


def downgrade():
    op.drop_table("buoys")

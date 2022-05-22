"""Create coastlines

Revision ID: 6fc1a99cefd5
Revises: d632ea3490c4
Create Date: 2022-05-21 14:48:54.624485

"""
from alembic import op
from geoalchemy2.types import Geography
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "6fc1a99cefd5"
down_revision = "d632ea3490c4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "coastlines",
        sa.Column(
            "id",
            sa.Integer(),
            index=True,
            nullable=False,
            primary_key=True,
            unique=True,
        ),
        sa.Column(
            "geom",
            Geography(
                srid=4326, from_text="ST_GeogFromText", name="geography", nullable=False
            ),
            nullable=False,
        ),
        sa.Column(
            "station_id",
            sa.String(length=10),
            sa.ForeignKey("buoys.station_id"),
            nullable=False,
        ),
    )
    # op.create_index(
    #     "idx_coastlines_geom",
    #     "coastlines",
    #     ["geom"],
    #     unique=False,
    #     postgresql_using="gist",
    #     postgresql_ops={},
    # )
    # op.create_index(op.f("ix_coastlines_id"), "coastlines", ["id"], unique=False)


def downgrade():
    # op.drop_index(
    #     "idx_coastlines_geom",
    #     table_name="coastlines",
    #     postgresql_using="gist",
    #     postgresql_ops={},
    # )
    # op.drop_index(op.f("ix_coastlines_id"), table_name="coastlines")
    op.drop_table("coastlines")

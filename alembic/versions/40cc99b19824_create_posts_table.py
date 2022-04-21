"""create posts table

Revision ID: 40cc99b19824
Revises: 
Create Date: 2022-04-20 18:32:50.314246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40cc99b19824'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('test', sa.Column('id', sa.INTEGER, nullable=False,
                    primary_key=True), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('test')
    pass

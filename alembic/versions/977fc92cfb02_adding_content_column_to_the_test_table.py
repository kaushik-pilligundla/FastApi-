"""adding content column to the test table

Revision ID: 977fc92cfb02
Revises: 40cc99b19824
Create Date: 2022-04-20 18:53:15.549939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '977fc92cfb02'
down_revision = '40cc99b19824'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('test', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('test', 'content')
    pass

"""empty message

Revision ID: 01796f0999ba
Revises: 01fb0843a63c
Create Date: 2022-11-29 04:48:59.655239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01796f0999ba'
down_revision = '01fb0843a63c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('isPaidAfterGetted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'isPaidAfterGetted')
    # ### end Alembic commands ###

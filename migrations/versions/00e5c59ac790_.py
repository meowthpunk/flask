"""empty message

Revision ID: 00e5c59ac790
Revises: 01796f0999ba
Create Date: 2022-11-29 05:09:24.435816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e5c59ac790'
down_revision = '01796f0999ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('paidTime', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'paidTime')
    # ### end Alembic commands ###

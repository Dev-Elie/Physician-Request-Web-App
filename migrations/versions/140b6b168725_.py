"""empty message

Revision ID: 140b6b168725
Revises: 2ede7a9a8dc6
Create Date: 2021-07-12 17:53:32.483128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '140b6b168725'
down_revision = '2ede7a9a8dc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'status')
    # ### end Alembic commands ###

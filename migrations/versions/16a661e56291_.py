"""empty message

Revision ID: 16a661e56291
Revises: 6b43ddd9292f
Create Date: 2021-07-22 20:59:57.590627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a661e56291'
down_revision = '6b43ddd9292f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', sa.String(length=150), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=20), nullable=False))
    op.add_column('user', sa.Column('sex', sa.String(length=20), nullable=False))
    op.add_column('user', sa.Column('speciality', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'status')
    op.drop_column('user', 'speciality')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'location')
    op.drop_column('user', 'image')
    # ### end Alembic commands ###
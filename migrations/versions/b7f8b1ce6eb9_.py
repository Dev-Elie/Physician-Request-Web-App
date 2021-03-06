"""empty message

Revision ID: b7f8b1ce6eb9
Revises: e58d65b54195
Create Date: 2021-07-21 13:27:19.001219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f8b1ce6eb9'
down_revision = 'e58d65b54195'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trucks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trucks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('regno', sa.VARCHAR(length=100), nullable=False),
    sa.Column('truck_img', sa.VARCHAR(length=150), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('size', sa.VARCHAR(length=150), nullable=True),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

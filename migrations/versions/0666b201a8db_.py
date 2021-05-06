"""empty message

Revision ID: 0666b201a8db
Revises: 
Create Date: 2021-05-06 16:48:43.383065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0666b201a8db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('water_temp', sa.Float(), nullable=False),
    sa.Column('uv_level', sa.String(), nullable=False),
    sa.Column('uv_time', sa.Integer(), nullable=False),
    sa.Column('weather_conditions', sa.Float(), nullable=False),
    sa.Column('outside_temp', sa.Float(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    op.drop_table('pool')
    # ### end Alembic commands ###

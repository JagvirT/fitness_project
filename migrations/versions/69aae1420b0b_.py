"""empty message

Revision ID: 69aae1420b0b
Revises: 6016ee7ddcc3
Create Date: 2023-01-14 22:05:36.567296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69aae1420b0b'
down_revision = '6016ee7ddcc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('bodyPart', sa.String(length=150), nullable=True),
    sa.Column('target', sa.String(), nullable=True),
    sa.Column('equipment', sa.String(), nullable=True),
    sa.Column('gifUrl', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###

"""empty message

Revision ID: a673130a95e3
Revises: 69aae1420b0b
Create Date: 2023-01-19 14:45:26.026449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a673130a95e3'
down_revision = '69aae1420b0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.Column('sugar', sa.Integer(), nullable=True),
    sa.Column('serving_size', sa.Integer(), nullable=True),
    sa.Column('sodium', sa.Integer(), nullable=True),
    sa.Column('potassium_mg', sa.Integer(), nullable=True),
    sa.Column('saturated_fat', sa.Integer(), nullable=True),
    sa.Column('total_fat', sa.Integer(), nullable=True),
    sa.Column('calories', sa.Integer(), nullable=True),
    sa.Column('cholesterol_mg', sa.Integer(), nullable=True),
    sa.Column('protein', sa.Integer(), nullable=True),
    sa.Column('carbs', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food')
    # ### end Alembic commands ###

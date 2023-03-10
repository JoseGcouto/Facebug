"""empty message

Revision ID: 58c85ebfbb60
Revises: 76b7304f89a6
Create Date: 2023-01-19 20:10:45.302893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c85ebfbb60'
down_revision = '76b7304f89a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('Password', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follow')
    op.drop_table('Posts')
    op.drop_table('users')
    # ### end Alembic commands ###

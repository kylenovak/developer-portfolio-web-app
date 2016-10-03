"""empty message

Revision ID: 6cf922c46545
Revises: c2f37a0ef6f6
Create Date: 2016-10-03 01:17:46.777487

"""

# revision identifiers, used by Alembic.
revision = '6cf922c46545'
down_revision = 'c2f37a0ef6f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('_password', sa.String(), nullable=True),
    sa.Column('_salt', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
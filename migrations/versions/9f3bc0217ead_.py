"""empty message

Revision ID: 9f3bc0217ead
Revises: f85ac54e3535
Create Date: 2016-12-11 05:12:55.987152

"""

# revision identifiers, used by Alembic.
revision = '9f3bc0217ead'
down_revision = 'f85ac54e3535'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('create_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('update_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='contact_pkey')
    )
    ### end Alembic commands ###
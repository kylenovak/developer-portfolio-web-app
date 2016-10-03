"""empty message

Revision ID: efbbffddce15
Revises: d13d2f3c0a57
Create Date: 2016-10-01 23:25:28.972148

"""

# revision identifiers, used by Alembic.
revision = 'efbbffddce15'
down_revision = 'd13d2f3c0a57'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'result_all')
    op.drop_column('results', 'result_no_stop_words')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('result_no_stop_words', postgresql.JSON(), autoincrement=False, nullable=True))
    op.add_column('results', sa.Column('result_all', postgresql.JSON(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
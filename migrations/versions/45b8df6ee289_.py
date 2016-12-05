"""empty message

Revision ID: 45b8df6ee289
Revises: 43e970a67525
Create Date: 2016-12-02 22:59:03.418749

"""

# revision identifiers, used by Alembic.
revision = '45b8df6ee289'
down_revision = '43e970a67525'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resume', sa.Column('resume_content', postgresql.JSON(), nullable=False))
    op.drop_column('resume', 'content')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resume', sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('resume', 'resume_content')
    ### end Alembic commands ###

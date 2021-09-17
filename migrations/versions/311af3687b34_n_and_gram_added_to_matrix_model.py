"""n and gram added to matrix model

Revision ID: 311af3687b34
Revises: 1cdb66a88b9b
Create Date: 2021-09-16 21:34:45.044136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311af3687b34'
down_revision = '1cdb66a88b9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matrix', sa.Column('n', sa.Integer(), nullable=False))
    op.add_column('matrix', sa.Column('gram', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('matrix', 'gram')
    op.drop_column('matrix', 'n')
    # ### end Alembic commands ###
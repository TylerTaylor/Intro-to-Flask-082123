"""Update appointment table to include date

Revision ID: 317b02e418e4
Revises: cc8c361c65ce
Create Date: 2023-10-24 13:13:43.419205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317b02e418e4'
down_revision = 'cc8c361c65ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
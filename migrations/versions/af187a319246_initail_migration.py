"""initail migration

Revision ID: af187a319246
Revises: 
Create Date: 2024-12-13 22:10:54.468712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af187a319246'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tax_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_date', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('due_date', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tax_record')
    # ### end Alembic commands ###

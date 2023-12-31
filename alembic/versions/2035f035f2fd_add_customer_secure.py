"""add customer secure

Revision ID: 2035f035f2fd
Revises: 8b24c4cdc30b
Create Date: 2023-08-09 16:08:25.860620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2035f035f2fd'
down_revision = '8b24c4cdc30b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('mail', sa.String(length=100), nullable=True))
    op.add_column(
        'customers', sa.Column('password', sa.String(length=64), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'password')
    op.drop_column('customers', 'mail')
    # ### end Alembic commands ###

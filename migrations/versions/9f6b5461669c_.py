"""empty message

Revision ID: 9f6b5461669c
Revises: 6004b28e21e2
Create Date: 2019-05-23 22:43:58.598519

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f6b5461669c'
down_revision = '6004b28e21e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.alter_column('employees', 'is_admin',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'is_admin',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('employees', 'password_hash')
    # ### end Alembic commands ###
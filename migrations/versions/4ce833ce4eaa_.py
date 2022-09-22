"""empty message

Revision ID: 4ce833ce4eaa
Revises: 931ee0b65ede
Create Date: 2022-09-22 10:38:51.616833

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ce833ce4eaa'
down_revision = '931ee0b65ede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    op.add_column('car', sa.Column('name', sa.String(length=100), nullable=True))
    op.add_column('car', sa.Column('selling_price', sa.Float(), nullable=True))
    op.drop_column('car', 'make')
    op.drop_column('car', 'color')
    op.drop_column('car', 'model')
    op.drop_column('car', 'price')
    op.drop_column('car', 'date_created')
    op.add_column('post', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_created')
    op.add_column('car', sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('model', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('color', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('make', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_column('car', 'selling_price')
    op.drop_column('car', 'name')
    op.create_table('blog',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('body', sa.VARCHAR(length=1200), autoincrement=False, nullable=True),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='blog_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='blog_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blog_pkey')
    )
    # ### end Alembic commands ###

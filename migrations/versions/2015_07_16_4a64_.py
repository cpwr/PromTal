"""empty message

Revision ID: 4a64396b1dc
Revises: None
Create Date: 2015-07-16 17:14:05.489738

"""

# revision identifiers, used by Alembic.
revision = '4a64396b1dc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['news_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=True),
    sa.Column('full_name', sa.String(length=64), nullable=True),
    sa.Column('mobile_phone', sa.String(), nullable=True),
    sa.Column('inner_phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('quote_for_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['quote_for_id'], ['comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['news_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_comment_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_tag_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['news_tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_tag_association')
    op.drop_table('news_comment_association')
    op.drop_table('news')
    op.drop_table('comment')
    op.drop_table('users')
    op.drop_table('news_tag')
    op.drop_table('news_category')
    ### end Alembic commands ###
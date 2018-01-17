"""init database

Revision ID: 80f27fe2be7b
Revises: 
Create Date: 2018-01-17 09:10:47.341646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f27fe2be7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyname', sa.String(length=64), nullable=False),
    sa.Column('logo', sa.String(length=128), nullable=True),
    sa.Column('website', sa.String(length=128), nullable=False),
    sa.Column('address', sa.String(length=32), nullable=False),
    sa.Column('intro', sa.String(length=512), nullable=False),
    sa.Column('desc', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('logo')
    )
    op.create_index(op.f('ix_company_address'), 'company', ['address'], unique=False)
    op.create_index(op.f('ix_company_companyname'), 'company', ['companyname'], unique=True)
    op.create_index(op.f('ix_company_intro'), 'company', ['intro'], unique=False)
    op.create_index(op.f('ix_company_website'), 'company', ['website'], unique=True)
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jobname', sa.String(length=32), nullable=True),
    sa.Column('salary', sa.String(length=32), nullable=True),
    sa.Column('exprequirement', sa.String(length=32), nullable=True),
    sa.Column('edurequirement', sa.String(length=32), nullable=True),
    sa.Column('address', sa.String(length=32), nullable=True),
    sa.Column('desc', sa.String(length=512), nullable=True),
    sa.Column('requirement', sa.String(length=512), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_job_jobname'), 'job', ['jobname'], unique=True)
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_job_jobname'), table_name='job')
    op.drop_table('job')
    op.drop_index(op.f('ix_company_website'), table_name='company')
    op.drop_index(op.f('ix_company_intro'), table_name='company')
    op.drop_index(op.f('ix_company_companyname'), table_name='company')
    op.drop_index(op.f('ix_company_address'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###

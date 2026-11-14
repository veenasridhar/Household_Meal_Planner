"""change cooking instructions datatype

Revision ID: af6b0e9fc486
Revises: 
Create Date: 2026-11-14 17:35:58.505089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af6b0e9fc486'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('recipemodel', 'cooking_time', existing_type=sa.Float(), type_=sa.String(), existing_nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('recipemodel', 'cooking_time', existing_type=sa.String(), type_=sa.Float(), existing_nullable=False)

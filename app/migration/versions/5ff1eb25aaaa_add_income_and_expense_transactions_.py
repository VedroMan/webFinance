"""add income and expense transactions, wallet

Revision ID: 5ff1eb25aaaa
Revises: 07599da7ea6e
Create Date: 2025-05-15 23:01:35.959251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ff1eb25aaaa'
down_revision: Union[str, None] = '07599da7ea6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

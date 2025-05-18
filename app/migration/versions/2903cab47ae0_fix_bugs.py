"""fix bugs

Revision ID: 2903cab47ae0
Revises: 5ff1eb25aaaa
Create Date: 2025-05-16 20:04:46.662103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2903cab47ae0'
down_revision: Union[str, None] = '5ff1eb25aaaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

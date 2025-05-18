"""update balance column

Revision ID: 1795a9c2b0c7
Revises: 2903cab47ae0
Create Date: 2025-05-17 19:53:09.853160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1795a9c2b0c7'
down_revision: Union[str, None] = '2903cab47ae0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass


"""Import every model here so SQLAlchemy and Alembic register it on Base.metadata."""

from app.models.customer import Customer
from app.models.product import Product

__all__ = ["Customer", "Product"]
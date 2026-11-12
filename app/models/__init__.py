"""Import every model here so SQLAlchemy and Alembic register it on Base.metadata."""

from app.models.customer import Customer

__all__ = ["Customer"]
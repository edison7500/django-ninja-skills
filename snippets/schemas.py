from datetime import datetime
from typing import List, Optional
from uuid import UUID
from ninja import Schema, ModelSchema
from pydantic import Field, validator
from .models import Product, Category


# 1. Standard Pydantic Schema (Non-Model based)
class Message(Schema):
    """Simple message schema for API responses like errors."""

    message: str
    code: Optional[str] = None


# 2. Model-based Schemas
class CategoryOut(ModelSchema):
    """Schema for Category, mapped directly from Django Model."""

    class Config:
        model = Category
        model_fields = ["id", "name", "slug"]


class ProductIn(ModelSchema):
    """
    Input Schema for creating/updating a Product.
    Explicitly excludes system-generated fields like id and timestamps.
    """

    category_id: int = Field(..., description="The ID of the related category")
    status: Product.Status = Field(
        ...,
        description="product status",
        examples=[Product.Status.ACTIVE],
    )

    class Config:
        model = Product
        model_fields = ["name", "description", "price", "inventory_count"]


class ProductOut(ModelSchema):
    """
    Output Schema for Product.
    Includes nested data and custom computed fields.
    """

    # Nested relationship
    category: Optional[CategoryOut] = Field(None, description="product category")

    # Custom field not directly in model_fields (calculated or alias)
    is_in_stock: bool

    class Config:
        model = Product
        model_fields = [
            "id",
            "name",
            "description",
            "status",
            "price",
            "inventory_count",
            "created_at",
        ]

    # Resolver for custom fields (Ninja's way to handle extra logic)
    @staticmethod
    def resolve_is_in_stock(obj):
        return obj.inventory_count > 0


# 3. Advanced Filtering/Search Schema
class ProductFilter(Schema):
    """Schema for query parameters in list views."""

    query: Optional[str] = None
    category_id: Optional[int] = None
    status: Product.Status = Field(
        ...,
        description="product status",
        examples=[Product.Status.ACTIVE],
    )
    min_price: Optional[float] = Field(None, ge=0)
    max_price: Optional[float] = None
    order_by: str = "created_at"


# 4. Auth/Token Schemas
class TokenOut(Schema):
    access_token: str
    token_type: str = "bearer"
    user_id: int

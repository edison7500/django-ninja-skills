from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, Query
from ninja.pagination import paginate
from .models import Product
from .schemas import ProductIn, ProductOut, ProductFilter, Message

# 1. Initialize Router with Tags for Clean OpenAPI Docs
router = Router(tags=["Products"])


# --- READ (List) ---
@router.get("/", response=List[ProductOut])
@paginate  # Ninja built-in pagination
async def list_products(request, filters: Query[ProductFilter]):
    """
    Retrieve a paginated list of products using Async QuerySets.
    """
    # Note: .all() is lazy, pagination handles the async evaluation if configured
    qs = Product.objects.all()

    if filters.category_id:
        qs = qs.filter(category_id=filters.category_id)

    order_by = (
        filters.order_by.value
        if hasattr(filters.order_by, "value")
        else filters.order_by
    )

    return qs.order_by(order_by)


# --- READ (Detail) ---
@router.get("/{product_id}", response={200: ProductOut, 404: Message})
async def get_product(request, product_id: int):
    """
    Fetch a single product. Demonstrates handling 404 via custom response.
    """
    try:
        # Django 5.0+ supports aget_object_or_404 or manual aget
        return await Product.objects.aget(id=product_id)
    except Product.DoesNotExist:
        return 404, {"message": f"Product {product_id} not found"}


# --- CREATE ---
@router.post("/", response={201: ProductOut})
async def create_product(request, data: ProductIn):
    """
    Create a new product using the validated Pydantic In-Schema.
    """
    product = await Product.objects.acreate(**data.dict())
    return 201, product


# --- UPDATE ---
@router.put("/{product_id}", response={200: ProductOut, 404: Message})
async def update_product(request, product_id: int, data: ProductIn):
    """
    Update an existing product. Uses aget and asave for full async flow.
    """
    try:
        product = await Product.objects.aget(id=product_id)
        for attr, value in data.dict().items():
            setattr(product, attr, value)
        await product.asave()
        return product
    except Product.DoesNotExist:
        return 404, {"message": "Product not found"}


# --- DELETE ---
@router.delete("/{product_id}", response={204: None, 404: Message})
async def delete_product(request, product_id: int):
    """
    Delete a product. Returns 204 No Content on success.
    """
    try:
        product = await Product.objects.aget(id=product_id)
        await product.adelete()
        return 204, None
    except Product.DoesNotExist:
        return 404, {"message": "Product not found"}

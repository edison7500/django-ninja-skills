"""
This snippet provides direct comparisons between anti-patterns and
Django Ninja best practices to guide the Agent's code generation logic.
"""

from ninja import Router, Schema, ModelSchema
from .models import Order
from django.shortcuts import get_object_or_404

router = Router(tags=["Comparison"])

# ==========================================
# 1. RESPONSE HANDLING
# ==========================================


# ❌ BAD: Returning raw dictionaries or manual JsonResponse
@router.get("/bad-response/{id}")
def bad_response(request, id: int):
    order = get_object_or_404(Order, id=id)
    return {"id": order.id, "status": order.status}  # No validation, no documentation


# ✅ GOOD: Explicit response schemas for type safety and auto-docs
class OrderOut(ModelSchema):
    class Config:
        model = Order
        model_fields = ["id", "status", "total"]


@router.get("/good-response/{id}", response=OrderOut)
def good_response(request, id: int):
    return get_object_or_404(Order, id=id)


# ==========================================
# 2. ASYNC USAGE
# ==========================================


# ❌ BAD: Using sync views for I/O bound tasks in a modern stack
@router.get("/bad-async")
def bad_sync_view(request):
    data = Order.objects.all()  # Blocks the worker
    return list(data)


# ✅ GOOD: Utilizing async def with Django's async ORM
@router.get("/good-async", response=list[OrderOut])
async def good_async_view(request):
    return [order async for order in Order.objects.all()]


# ==========================================
# 3. ERROR HANDLING
# ==========================================

# ❌ BAD: Manual try-except with hardcoded JsonResponse
from django.http import JsonResponse


@router.post("/bad-error")
def bad_error(request, data: dict):
    if "item_id" not in data:
        return JsonResponse({"error": "Missing ID"}, status=400)


# ✅ GOOD: Using Ninja HttpError for standardized exceptions
from ninja.errors import HttpError


@router.post("/good-error")
def good_error(request, data: OrderOut):
    if not data.id:
        raise HttpError(400, "Order ID is mandatory for this operation")
    return data


# ==========================================
# 4. AUTHENTICATION
# ==========================================


# ❌ BAD: Checking user status inside the function body
@router.get("/bad-auth")
def bad_auth(request):
    if not request.user.is_authenticated:
        return {"error": "Forbidden"}, 403
    return {"message": "Success"}


# ✅ GOOD: Decoupling security via Router/API auth dependencies
from ninja.security import APIKeyHeader


class ApiKeyAuth(APIKeyHeader):
    def authenticate(self, request, key):
        if key == "secret-token":
            return key


router_secure = Router(auth=ApiKeyAuth())


@router_secure.get("/good-auth")
def good_auth(request):
    return {"message": "Authenticated via dependency injection"}

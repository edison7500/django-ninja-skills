from django.contrib.auth.models import User
from django.http import HttpRequest
from ninja.security import APIKeyHeader, HttpBearer
from ninja.errors import HttpError
from typing import Optional


# 1. API Key Authentication (e.g., for Internal Service-to-Service)
class ApiKeyAuth(APIKeyHeader):
    param_name: str = "X-API-Key"

    def authenticate(self, request: HttpRequest, key: str) -> Optional[str]:
        # In production, fetch this from settings or a database
        if key == "super-secret-internal-key":
            return key
        return None


# 2. JWT / Bearer Token Authentication (Standard Web Auth)
class JWTAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[User]:
        """
        Logic to decode JWT and return a User object.
        Ninja automatically attaches the return value to 'request.auth'.
        """
        try:
            # Placeholder for JWT decoding logic (e.g., using PyJWT)
            # user = decode_token_and_get_user(token)
            user = User.objects.get(username="demo_user")  # Mock for example
            return user
        except Exception:
            # Returning None triggers a 401 Unauthorized
            return None


# 3. Role-Based Access Control (RBAC) Pattern
class RoleChecker:
    def __init__(self, role: str):
        self.role = role

    def __call__(self, request: HttpRequest):
        # Assumes user is already authenticated by another provider
        user = request.auth
        if not user or not user.is_authenticated:
            raise HttpError(401, "Authentication required")

        if self.role == "admin" and not user.is_staff:
            raise HttpError(403, "Admin privileges required")

        return user


# --- USAGE EXAMPLES ---

# Case A: Global Router Auth
# from ninja import Router
# router = Router(auth=JWTAuth())

# Case B: Per-Endpoint Auth Override
# @router.get("/secret", auth=ApiKeyAuth())
# def secret_data(request):
#     return {"data": "confidential"}

# Case C: Multiple Auth Methods (OR logic)
# @router.get("/flexible", auth=[JWTAuth(), ApiKeyAuth()])
# def flexible_auth(request):
#     return {"user": str(request.auth)}

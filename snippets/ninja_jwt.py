# 1. django-ninja-jwt Settings

from datetime import timedelta
from django.conf import settings

NINJA_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "ninja_jwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("ninja_jwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "ninja_jwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # For Controller Schemas
    # FOR OBTAIN PAIR
    "TOKEN_OBTAIN_PAIR_INPUT_SCHEMA": "ninja_jwt.schema.TokenObtainPairInputSchema",
    "TOKEN_OBTAIN_PAIR_REFRESH_INPUT_SCHEMA": "ninja_jwt.schema.TokenRefreshInputSchema",
    # FOR SLIDING TOKEN
    "TOKEN_OBTAIN_SLIDING_INPUT_SCHEMA": "ninja_jwt.schema.TokenObtainSlidingInputSchema",
    "TOKEN_OBTAIN_SLIDING_REFRESH_INPUT_SCHEMA": "ninja_jwt.schema.TokenRefreshSlidingInputSchema",
    "TOKEN_BLACKLIST_INPUT_SCHEMA": "ninja_jwt.schema.TokenBlacklistInputSchema",
    "TOKEN_VERIFY_INPUT_SCHEMA": "ninja_jwt.schema.TokenVerifyInputSchema",
}

# 2.  Route Authentication—Class Based
from ninja_extra import api_controller, route
from ninja_jwt.authentication import JWTAuth


@api_controller
class MyController:
    @route.get("/some-endpoint", auth=JWTAuth())
    def some_endpoint(self): ...


# 3. Route Authentication—Function Based
from ninja import router
from ninja_jwt.authentication import JWTAuth

router = router("")


@router.get("/some-endpoint", auth=JWTAuth())
def some_endpoint(request): ...


# 4. Custom Auth Implementation
from ninja.security import APIKeyHeader
from ninja_jwt.authentication import JWTBaseAuthentication
from ninja import router


class ApiKey(APIKeyHeader, JWTBaseAuthentication):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        return self.jwt_authenticate(request, token=key)


header_key = ApiKey()
router = router("")


@router.get("/headerkey", auth=header_key)
def apikey(request):
    return f"Token = {request.auth}"


# 5. Asynchronous Route Authentication
from ninja_extra import api_controller, route
from ninja_jwt.authentication import AsyncJWTAuth


@api_controller
class MyController:
    @route.get("/some-endpoint", auth=AsyncJWTAuth())
    async def some_endpoint(self): ...


# 6. Blacklist App

INSTALLED_APPS = [
    "ninja_jwt.token_blacklist",
]

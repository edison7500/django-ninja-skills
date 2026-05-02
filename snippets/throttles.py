# 1. Global Throttling
"""
If you want to apply a basic rate limit to the entire API, you can pass the `throttle` parameter directly when instantiating NinjaAPI.

In your main API file (e.g., `api.py`):
"""

from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle, UserRateThrottle

# 设置：匿名用户每分钟最多 10 次，登录用户每分钟最多 60 次
api = NinjaAPI(throttle=[AnonRateThrottle("10/m"), UserRateThrottle("60/m")])


@api.get("/hello")
def hello(request):
    return {"message": "Hello World"}


# 2. Router-Level Throttling
"""
In large projects, routers are typically organized by module. You can configure throttling separately for a specific module (such as a query module that consumes a lot of resources).

Create a file named something like routers/throttling_demo.py:    
"""
from ninja import Router
from ninja.throttling import AnonRateThrottle

# 仅对这个 router 下的所有接口限制为每秒 2 次请求
router = Router(throttle=[AnonRateThrottle("2/s")])


@router.get("/data1")
def get_data1(request):
    return {"data": "This is rate limited at 2 requests per second."}


@router.get("/data2")
def get_data2(request):
    return {"data": "This is ALSO rate limited at 2 requests per second."}


# 3. Endpoint-Level Throttling
"""
Sometimes you only need to protect a specific endpoint (such as the one for sending verification codes or the login endpoint).
In such cases, you can override the `throttle` parameter directly in the route decorator.
"""
from ninja import Router
from ninja.throttling import AnonRateThrottle

router = Router()


# 发送短信验证码接口，限制每个 IP 每天只能请求 5 次
@router.post("/send-code", throttle=[AnonRateThrottle("5/d")])
def send_sms_code(request, phone: str):
    # 发送逻辑...
    return {"success": True, "message": f"Code sent to {phone}"}


# 这个接口没有限流（除非全局配置了）
@router.get("/public-info")
def public_info(request):
    return {"info": "Unlimited access"}


# 💡 Rate Format Guide
"""
Django Ninja supports highly flexible rate expressions in the format “count/time unit”:

s = seconds (e.g., '10/s')
m = minutes (e.g., '100/m')
h = hours (e.g., '1000/h')
d = days (e.g., '5000/d')
"""

# 🛠️ How to Test Your Rate Limiting?
"""
Once integration is complete, you can start your Django service and quickly refresh the endpoint in a browser or using a tool like curl. When the limit is exceeded, Django Ninja will automatically intercept the request and return the standard HTTP status code: 429 Too Many Requests.

{
  "detail": "Request was throttled. Expected available in 58 seconds."
}
"""

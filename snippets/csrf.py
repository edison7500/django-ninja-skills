# 1. Use Django's built-in CSRF protection
from ninja import NinjaAPI
from ninja.security import APIKeyCookie


class CookieAuth(APIKeyCookie):
    def authenticate(self, request, key):
        return key == "test"


api = NinjaAPI(auth=CookieAuth())


# 2. django-auth based (which is inherited from cookie based auth)
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth)


# 3. Django ensure_csrf_cookie decorator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@api.post("/csrf")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request):
    return HttpResponse()

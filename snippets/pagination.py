from typing import List
from ninja import api
from ninja.pagination import paginate
from .models import User


# 1. To apply pagination to a function - just apply paginate decorator:
@api.get("/users", response=List[UserSchema])
@paginate
def list_users(request):
    return User.objects.all()


# 2. LimitOffsetPagination (default)
from ninja.pagination import paginate, LimitOffsetPagination


@api.get("/users", response=List[UserSchema])
@paginate(LimitOffsetPagination)
def list_users(request):
    return User.objects.all()


# 3. PageNumberPagination
from ninja.pagination import paginate, PageNumberPagination


@api.get("/users", response=List[UserSchema])
@paginate(PageNumberPagination)
def list_users(request):
    return User.objects.all()


# 4. CursorPagination
from ninja.pagination import paginate, CursorPagination


@api.get("/events", response=List[EventSchema])
@paginate(CursorPagination)
def list_events(request):
    return Event.objects.all()


# 5. Accessing paginator parameters in view function
@api.get("/someview")
@paginate(pass_parameter="pagination_info")
def someview(request, **kwargs):
    page = kwargs["pagination_info"].page
    return ...


# 6. Creating Custom Pagination Class
from ninja.pagination import paginate, PaginationBase
from ninja import Schema


class CustomPagination(PaginationBase):
    # only `skip` param, defaults to 5 per page
    class Input(Schema):
        skip: int

    class Output(Schema):
        items: List[Any]  # `items` is a default attribute
        total: int
        per_page: int

    def paginate_queryset(self, queryset, pagination: Input, **params):
        skip = pagination.skip
        return {
            "items": queryset[skip : skip + 5],
            "total": queryset.count(),
            "per_page": 5,
        }


@api.get("/users", response=List[UserSchema])
@paginate(CustomPagination)
def list_users(request):
    return User.objects.all()

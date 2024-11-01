from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, UserCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path('login/', TokenObtainPairView.as_view(pagination_class=AllowAny), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(pagination_class=AllowAny), name='token_refresh'),
]

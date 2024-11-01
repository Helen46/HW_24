from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, UserCreateAPIView, UserRetrieveApiView, UserUpdateApiView, \
    UserDestroyApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user/update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDestroyApiView.as_view(), name="user_delete"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create")
]

urlpatterns += router.urls

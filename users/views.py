from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializer import UserSerializer, PaymentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import RegisterSerializer


class RegisterCreateAPIView(generics.CreateAPIView):
    """
    Класс регистрации пользователя
    """

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
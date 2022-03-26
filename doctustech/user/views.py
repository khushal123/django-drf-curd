from rest_framework.generics import CreateAPIView
from doctustech.user.serializers import UserSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Create your views here.


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

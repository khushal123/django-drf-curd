from rest_framework.generics import CreateAPIView, UpdateAPIView
from doctustech.user.models import User
from doctustech.user.serializers import ActivateSerializer, UserSerializer, UserUpdateSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Create your views here.


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class ActivateView(UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        print(request.data)
        try:
            data = request.data
            serializer = ActivateSerializer(data)
            if serializer.is_valid:
                email = data.get("email")
                activation_token = data.get("activation_token")
                user = User.objects.get(email=email, activation_token=activation_token)
                user.is_active = True
                user.activation_token = False
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class UpdateUserView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from doctustech.post.serializers import PostSerializer
from doctustech.user.models import User
from doctustech.user.serializers import ActivateSerializer, UsereCreateSerializer, UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = UsereCreateSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def patch(self, request, id):
        user = self.get_object(id)
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ActivateUserView(UpdateAPIView):
    def post(self, request, format=None):
        print(request.data)
        try:
            data = request.data
            serializer = ActivateSerializer(data)
            if serializer.is_valid:
                email = data.get("email")
                activation_token = data.get("activation_token")
                try:
                    user = User.objects.get(email=email, activation_token=activation_token)
                    user.is_active = True
                    user.activation_token = False
                    user.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    return Response({}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class PostView(ListAPIView):

    def get(self, request, id):
        serializer = PostSerializer(post_by=id)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
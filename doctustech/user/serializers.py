from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from doctustech.user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from base64 import b64encode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password", "activation_token"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        validated_data['activation_token'] = b64encode(
            validated_data.get("email").encode('utf-8')).decode("utf-8")
        validated_data["password"] = make_password(
            validated_data.get("password"))
        return User.objects.create(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        required=True
    )


class ActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_active"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_status"]

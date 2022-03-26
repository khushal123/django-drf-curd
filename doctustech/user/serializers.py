from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from doctustech.user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all(), message="email already exists")]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        max_length=30
    )

    class Meta:
        model = User
        fields = ["name", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return User.objects.create(**validated_data)



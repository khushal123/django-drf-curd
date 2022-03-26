from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from doctustech.user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
        fields = ["first_name", "last_name", "email", "password"]


class LoginSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
    def validate(self, attrs):
        data = super().validate(attrs)
        return data
from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from django.contrib.auth.hashers import check_password
from doctustech.user.models import User

class DrfBackend(BaseBackend):
    def authenticate(self, request: Optional[HttpRequest], **kwargs: Any):
        email = kwargs['email']
        password = kwargs["password"]
        try:
            print(kwargs)
            user = User.objects.filter(email=email).get()
            pwd_valid = check_password(password, user.password)
            if pwd_valid is False:
                return Exception("Invalid password")
            return user
        except User.DoesNotExist:
            raise Exception("User not found")
        return None


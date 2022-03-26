from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from django.contrib.auth.hashers import check_password
from doctustech.user.models import User

class DrfBackend(BaseBackend):
    def authenticate(self, request: Optional[HttpRequest], **kwargs: Any):
        print(kwargs)
        email = kwargs['email']
        password = kwargs["password"]
        try:
            user = User.objects.get(email=email)
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
            return None
        except User.DoesNotExist:
            return None


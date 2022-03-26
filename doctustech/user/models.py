from django.db.models import TextField, CharField, BooleanField, EmailField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    name = CharField(max_length=50)
    is_active = BooleanField(default=False)
    email = EmailField(max_length=50, unique=True)
    password = CharField(max_length=100)
    profile_status = CharField(max_length=100)
    profile_image = TextField()


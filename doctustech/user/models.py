from django.db.models import TextField
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    profile_status = CharField(max_length=100)
    profile_image = TextField()
    

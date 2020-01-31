from django.db import models
from django.contrib.auth.models import AbstractUser
from registration.validators import validate_phone


class User(AbstractUser):
    contact_no = models.CharField(max_length=13, validators=[validate_phone], null=True, blank=True)

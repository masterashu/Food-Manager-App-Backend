from django.db import models
from django.contrib.auth.models import AbstractUser
from menu.models import *
from registration.validators import validate_phone


class User(AbstractUser):
    name = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(unique=True, max_length=254)
    contact_no = models.CharField(max_length=13, validators=[validate_phone])
    meal_opted_out_from = models.ForeignKey(MealOptedOut, on_delete=models.CASCADE)
    feedback_given = models.ForeignKey(Feedback, on_delete=models.CASCADE)

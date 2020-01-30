from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["name", "email", "contact_no", "meal_opted_out_from", "feedback_given"]
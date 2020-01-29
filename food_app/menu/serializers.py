from rest_framework import serializers as sz
from .models import *


class FoodSerializer(sz.ModelSerializer):
    available = sz.BooleanField(source='availability')

    class Meta:
        model = Food
        fields = ['id', 'name', 'meal', 'description', 'available']


class MenuSerializer(sz.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['type', 'day', 'meal', 'food_items']


class MealOptedOutSerializer(sz.ModelSerializer):
    class Meta:
        model = MealOptedOut
        fields = ['date', 'type', 'user']


class FeedbackSerializer(sz.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['user', 'description', 'date', 'food']

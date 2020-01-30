from rest_framework import serializers as sz
from .models import *
from registration.serializers import UserSerializer


class FoodSerializer(sz.ModelSerializer):
    available = sz.BooleanField(source='availability')

    class Meta:
        model = Food
        fields = ['name', 'meal', 'description', 'available']


class MenuSerializer(sz.ModelSerializer):
    food_items = FoodSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['type', 'day', 'food_items']


class MealOptedOutSerializer(sz.ModelSerializer):
    user = UserSerializer()
    type = sz.CharField(source='get_type_display')

    class Meta:
        model = MealOptedOut
        fields = ['date', 'type', 'user']


class FeedbackSerializer(sz.ModelSerializer):
    user = UserSerializer()
    food = FoodSerializer()
    
    class Meta:
        model = Feedback
        fields = ['user', 'description', 'date', 'food']


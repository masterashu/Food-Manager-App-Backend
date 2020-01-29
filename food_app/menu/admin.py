from django.contrib import admin
from .models import *


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    model = Food


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu


@admin.register(MealOptedOut)
class MealOptedOutAdmin(admin.ModelAdmin):
    model = MealOptedOut


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    models = Feedback
    read_only_fields = ['user', 'description', 'date', 'food']


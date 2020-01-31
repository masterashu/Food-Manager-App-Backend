from django.db import models
from registration.models import User


class Food(models.Model):
    MEAL = (
        ("V", "Veg"),
        ("NV", "Non-Veg"),
    )

    id = models.CharField(max_length=10, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    meal = models.CharField(max_length=10, choices=MEAL, default="V")
    description = models.CharField(max_length=200)
    availability = models.BooleanField(default=True)


class Menu(models.Model):
    DAY = (
        ("0", "Sunday"),
        ("1", "Monday"),
        ("2", "Tuesday"),
        ("3", "Wednesday"),
        ("4", "Thursday"),
        ("5", "Friday"),
        ("6", "Saturday"),
    )

    TYPE = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE,
        default="B",
    )
    day = models.CharField(
        max_length=10,
        choices=DAY,
        default=1
    )
    food_items = models.ManyToManyField(Food)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['type', 'day'], name='unique_meal')
        ]


class MealOptedOut(models.Model):
    TYPE = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
    )
    date = models.DateField()
    type = models.CharField(
        max_length=10,
        choices=TYPE,
        default="B",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='opted_out_meals')


class Feedback(models.Model):
    TYPE = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feedback')
    description = models.CharField(max_length=500)
    date = models.DateField()
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='feedback')


class Extras(models.Model):
    TYPE = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
    )
    MEAL = (
        ("V", "Veg"),
        ("NV", "Non-Veg"),
    )
    id = models.CharField(max_length=10, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    meal = models.CharField(max_length=10, choices=MEAL, default="V")
    description = models.CharField(max_length=200)

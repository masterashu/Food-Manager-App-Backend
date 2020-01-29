from rest_framework.views import APIView, Response
from rest_framework.status import *
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from datetime import date


class MenuGetView(APIView):
    def get(self, request):
        menu = Menu.objects.all()
        menu_serialized = MenuSerializer(menu, many=True)
        return Response(menu_serialized.data, status=200)


class MealOptOutView(APIView):
    def get(self, request):
        meals = MealOptedOut.objects.filter(date__gte=date.today())
        meals_serialized = MealOptedOutSerializer(meals, many=True)
        return Response(meals_serialized.data, status=HTTP_200_OK)

    def post(self, request):
        return


class TodayMealOptOutView(APIView):
    def get(self, request):
        meals = MealOptedOut.objects.filter(date=date.today())
        meals_serialized = MealOptedOutSerializer(meals, many=True)
        return Response(meals_serialized.data, status=HTTP_200_OK)

from rest_framework.views import APIView, Response
from rest_framework.status import *
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


class TodayMealOptOutView(APIView):
    def get(self, request):
        meals = MealOptedOut.objects.filter(date=date.today())
        meals_serialized = MealOptedOutSerializer(meals, many=True)
        return Response(meals_serialized.data, status=HTTP_200_OK)


class FeedbackGivenView(APIView):
    def get(self, request):
        feedback = Feedback.objects.all()
        feedback_serialized = FeedbackSerializer(feedback, many=True)
        return Response(feedback_serialized.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MonthlyFeedbackGivenView(APIView):
    def get(self, request, month):
        feedback = Feedback.objects.filter(date__month=month)
        feedback_serialized = FeedbackSerializer(feedback, many=True)
        return Response(feedback_serialized.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


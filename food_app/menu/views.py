from rest_framework.views import APIView, Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrGet
from rest_framework.parsers import JSONParser
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from datetime import date, datetime, timedelta


class MenuGetView(APIView):
    def get(self, request):
        menu = Menu.objects.all()
        menu_serialized = MenuSerializer(menu, many=True)
        return Response(menu_serialized.data, status=200)


class MealOptOutView(APIView):
    permission_classes = [IsAuthenticatedOrGet, ]
    parser_classes = (JSONParser,)

    def get(self, request):
        meals = MealOptedOut.objects.filter(date__gte=date.today())
        meals_serialized = MealOptedOutSerializer(meals, many=True)
        return Response(meals_serialized.data, status=HTTP_200_OK)

    def post(self, request):
        d = request.data.get("date")
        t = request.data.get("type")
        d = datetime.strptime(d, "%d-%m-%Y")
        if d - datetime.now() > timedelta(days=1):
            if MealOptedOut.objects.filter(date=d.date(), user=request.user, type=t).count() == 0:
                m = MealOptedOut()
                m.date = d.date()
                m.user = request.user
                m.type = t
                m.save()
                data = MealOptedOutSerializer(m)
                return Response(data.data, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class TodayMealOptOutView(APIView):
    def get(self, request):
        meals = MealOptedOut.objects.filter(date=date.today())
        meals_serialized = MealOptedOutSerializer(meals, many=True)
        return Response(meals_serialized.data, status=HTTP_200_OK)


class FeedbackGivenView(APIView):
    permission_classes = [IsAuthenticated, ]

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


class ExtraOrderView(APIView):
    def get(self, request):
        extra_food = ExtrasOrder.objects.all()
        extra_food_serialized = ExtrasOrderSerializer(extra_food, many=True)
        return Response(extra_food_serialized, status=HTTP_200_OK)

    def post(self, request):
        serializer = ExtrasOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_200_OK)

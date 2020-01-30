from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


class UserAccountCreateView(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        serializer = UserSerializer(user_data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        if request.user is not None:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)

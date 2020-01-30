from django.urls import path
from .views import *

urlpattern = [
    path('createuser/', UserAccountCreateView.as_view(), name='api_create_user'),
    path('get_user_details/', UserDetailView.as_view(), name='api_user_details'),
]

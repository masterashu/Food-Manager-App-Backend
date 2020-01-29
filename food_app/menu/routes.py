from django.urls import path
from .views import *


urlpatterns = [
    path('opt_out/today/', TodayMealOptOutView.as_view(), name='api_opt_out_today'),
    path('opt_out/', MealOptOutView.as_view(), name='api_opt_out'),
    # path('',)
]

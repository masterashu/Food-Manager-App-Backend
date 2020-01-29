from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', MenuGetView.as_view(), name='api_get_menu'),
    path('opt_out/today/', TodayMealOptOutView.as_view(), name='api_opt_out_today'),
    path('opt_out/', MealOptOutView.as_view(), name='api_opt_out'),
    path('feedback/', FeedbackGivenView.as_view(), name='api_feedback_given'),
    path('feedback/<int:month>/', MonthlyFeedbackGivenView.as_view(), name='api_monthly_feedback_given'),
]

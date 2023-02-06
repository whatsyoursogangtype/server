from django.urls import path
from .views import StatisticView

urlpatterns = [
    path('stats/<int:pk>/', StatisticView.as_view()),
]

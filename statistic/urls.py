from django.urls import path
from .views import StatisticView, RankView

urlpatterns = [
    path('stats/<int:pk>/', StatisticView.as_view()),
    path('stats/rank/', RankView.as_view())
]

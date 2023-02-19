from django.urls import path
from .views import *

urlpatterns = [
    path('stats/<int:pk>/', StatisticView.as_view()),
    path('stats/rank/', RankView.as_view()),
    # path('stats/rankk/', RankkView.as_view())
]

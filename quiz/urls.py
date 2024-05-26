from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('result/<int:score>/', views.quiz_result, name='quiz_result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
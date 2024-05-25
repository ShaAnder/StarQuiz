from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.start_quiz, name='start_quiz'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
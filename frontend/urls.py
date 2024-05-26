from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('intro/', views.intro, name='intro'),
    path('galaxy/', views.galaxy_map, name='galaxy_map'),
    path('planet/<int:planet_id>/', views.planet_detail, name='planet_detail'),
]
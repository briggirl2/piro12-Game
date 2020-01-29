
from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('playgame/computer/', views.playgame_computer, name='playgame_computer'),
]

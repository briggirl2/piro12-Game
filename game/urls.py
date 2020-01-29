
from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('selectLogin/', views.select_login, name='select_login'),
    path('playgame/computer/', views.playgame_computer, name='playgame_computer'),
]

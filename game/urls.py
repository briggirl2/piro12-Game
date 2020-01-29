
from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('selectLogin/', views.select_login, name='select_login'),
    path('playgame/computer/', views.playgame_computer, name='playgame_computer'),
    path('gamelist/', views.gamelist, name='gamelist'),  # 게임 전적 보는 페이지
    path('gamedetail/<int:pk>', views.gamedetail, name='gamedetail'), #게임 전적 디테일 페이지


    # path('ready/', views.ready, name='ready'),
    path('challenge/', views.challenge, name='challenge'),
    path('ing/<int:pk>/', views.ing_challenge, name='ing_challenge'),
    path('mygame/', views.mygame, name='mygame'),
]

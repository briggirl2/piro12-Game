
from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),
    path('selectLogin/', views.select_login, name='select_login'),
    path('playgame/computer/', views.playgame_computer, name='playgame_computer'),
    # path('gamestart/', views.gamestart, name='gamestart'),  # 가위바위보하는 페이지
    path('gamelist/', views.gamelist, name='gamelist'),  # 게임 전적 보는 페이지
    path('gamedetail/<int:pk>', views.gamedetail, name='gamedetail'), #게임 전적 디테일 페이지
]
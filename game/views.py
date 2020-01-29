import random

import json
import requests
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse, HttpResponse

from .loginView import KakaoLoginView
from django.shortcuts import render


def home(request):
    return render(request, 'game/home.html')


def playgame_computer(request):
    if request.method == 'GET':
        return render(request, 'game/playgame_computer.html', {})
    elif request.method == 'POST':
        user1_input = request.POST['seleted_action']
        print(user1_input)
        user2_input = random.choice(['가위', '바위', '보']) #computer
        print(user2_input)
        game_result = makeresult(user1_input, user2_input) # 0무승부/1:1승리/2:2승리
        print(game_result)
        game_result_str = ['무승부', '승', '패'][game_result]
        print(game_result_str)
        context = {
            'user1_input': user1_input,
            'user2_input': user2_input,
            'game_result': game_result_str,
        }
        return render(request, "game/gameresult_computer.html", context)


def makeresult(a, b):
    if a == b:
        return 0 # 무승부
    elif a == '가위':
        if b == '바위':
            return 2
        elif b == '보':
            return 1
    elif a == '바위':
        if b == '보':
            return 2
        elif b == '가위':
            return 1
    elif a == '보':
        if b == '가위':
            return 2
        elif b == '바위':
            return 1


def select_login(request):
    return render(request, 'game/select_login.html')
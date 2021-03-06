import random

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from game.forms import ChallengeForm, AcceptChallengeForm
from game.models import Game


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
            'user1': '당신',
            'user2': '컴퓨터',
            'user1_input': user1_input,
            'user2_input': user2_input,
            'game_result': game_result_str,
        }
        return render(request, "game/gameresult_computer.html", context)


def makeresult(a, b):
    if a == b:
        return 0
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


def mygame(request):
    if not request.user.is_authenticated:
        return redirect('game:select_login')
    request.session['user_id'] = request.user.id
    games = Game.objects.filter(Q(defender=request.user.id) | Q(attacker=request.user.id)).order_by('-id')
    context = {
        'games': games,
    }
    return render(request, 'game/mygame.html', context)


def challenge(request):
    if request.method == 'POST':
        form = ChallengeForm(
            request.user, #현재 유저는 defender 목록에서 제외시키기 위해 인자로 지정 -> forms.py 13번째 username
            request.POST, #https://stackoverflow.com/questions/18184415/user-object-has-no-attribute-get
            #instance=args, initial= kwargs 둘다 필요없다. initial은 get타고 들어왔을때만 필요함.
        )
        if form.is_valid():
            user = get_user_model()
            print(form.cleaned_data['defender'])
            print(get_user_model().objects.filter)
            _attacker = user.objects.filter(username=request.user)[0].id
            _defender = user.objects.filter(username=form.cleaned_data['defender'])[0].id
            print(_attacker)
            print(form.cleaned_data['att_choice'], _attacker, _defender)
            g = Game.objects.create(
                att_choice=form.cleaned_data['att_choice'],
                attacker_id=_attacker,
                defender_id=_defender
            )

            #https://wayhome25.github.io/django/2017/05/06/django-form/
            #game.attacker.set(_attacker)
            #game.defender.set(_defender)
            #Direct assignment to the forward side of a many-to-many set is prohibited

            request.session['user_id'] = request.user.id
            games = Game.objects.filter(Q(defender=request.user.id) | Q(attacker=request.user.id))
            context = {
                'games': games,
            }
            return render(request, 'game/mygame.html', context)

    else:
        if request.user.is_authenticated:
            User = get_user_model()
            users = User.objects.all()
            other_users_cnt = users.count() - 1
            form = ChallengeForm(
                request.user, #여기로 get타고 들어와서 request.POST 빼버림.
                instance=request.user,
                initial={
                    'attacker': request.user.id,
                    # 'defender': request.session['opponent_id']
                },
                #수정시 placeholder가 아니라 initial를 설정하면 되는 것임!
            )
        else:
            return redirect('game:select_login')

    return render(request, 'game/challenge.html', {
        'form': form,
        'other_users_cnt': other_users_cnt,
    })


def ing_challenge(request, pk):
    if not request.user.is_authenticated:
        return redirect('game:select_login')
    game = get_object_or_404(Game, id=pk)
    form = AcceptChallengeForm(
        request.POST,
        instance=game
    )
    context = {
        'game': game,
        'form': form,
    }
    dict = {
        2: '바위',
        1: '가위',
        0: '보'
    }
    print(game.dfd_choice)
    if game.attacker == request.user:
        if game.dfd_choice is None:
            return render(request, 'game/not_yet.html', context)
        else:
            context = {
                'game': game,
                'form': form,
                'att_choice': dict[game.att_choice],
                'dfd_choice': dict[game.dfd_choice]
            }
            return render(request, 'game/result_challenge.html', context)
    else:
        if game.dfd_choice is None:
            if request.method == 'POST':
                if form.is_valid():
                    # user = get_user_model()
                    # print(form.cleaned_data['defender'])
                    # print(get_user_model().objects.filter)
                    # _attacker = user.objects.filter(username=request.user)[0].id
                    # _defender = user.objects.filter(username=form.cleaned_data['defender'])[0].id
                    # print(_attacker)
                    game = get_object_or_404(Game, id=pk)
                    Game.objects.filter(id=pk).update(
                        dfd_choice=form.cleaned_data['dfd_choice'],
                    )
                    point = game.att_choice - form.cleaned_data['dfd_choice']
                    print(point)
                    if point == 0:
                        pass
                    elif point == 1 or point == -2:
                        Game.objects.filter(id=pk).update(
                            winner=game.attacker,
                            loser=game.defender
                        )
                    else:
                        Game.objects.filter(id=pk).update(
                            winner=game.defender,
                            loser=game.attacker
                        )
                    #https://wayhome25.github.io/django/2017/05/06/django-form/
                    #game.attacker.set(_attacker)
                    #game.defender.set(_defender)
                    #Direct assignment to the forward side of a many-to-many set is prohibited
                    return redirect('game:ing_challenge', pk)
            return render(request, 'game/ing_challenge.html', context)
        else:
            context = {
                'game': game,
                'form': form,
                'att_choice': dict[game.att_choice],
                'dfd_choice': dict[game.dfd_choice]
            }
            return render(request, 'game/result_challenge.html', context)
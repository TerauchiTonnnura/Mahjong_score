from django.shortcuts import render
from django.http import Http404
from saki.forms import StartGame
from .models import Player, Game, Kyoku

from .forms import RonForm, TsumoForm, RyukyokuForm


def index(request):
    return render(request, 'saki/index.html')


def start_game(request):
    print(request.POST['game_type'])
    player_all = Player.objects.all()
    players = []
    for player in player_all:
        players.append((player.name, player.name),)
    f = StartGame(players)
    context = {'form': f}
    return render(request, 'saki/start_game.html', context)


def enter_kyoku_result(request):
    # if request.method == 'GET':
    #     raise Http404("Question does not exist")

    # To Do
    # request.POST に childd_point あるか check
    # if not 'child_point' in request.POST.keys():
    #   render index(request)

    # print(request.POST['child_point'])

    f_ron = RonForm()
    f_tsumo = TsumoForm()
    f_ryukyoku = RyukyokuForm()
    context = {
        'form_Ron': f_ron,
        'form_Tsumo': f_tsumo,
        'form_Ryukyoku': f_ryukyoku
    }

    # game = Game.objects.get(game_id=4)
    # tontya = game.ton
    return render(
        request,
        'saki/enter_kyoku_result.html',
        context
    )


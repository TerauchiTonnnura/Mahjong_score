from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .forms import StartGame
from .models import Player, Game, Kyoku, KyokuPlayer
from .mahjong_function import calc_stats

from .forms import RonForm, TsumoForm, RyukyokuForm, SearchStatsForm

game_oj = None
kyoku = 1
honba = 0
riichi_bou = 0


def index(request):
    return render(request, 'saki/index.html')


def start_game(request):
    if request.method == 'GET':
        player_all = Player.objects.all()
        players = []
        for player in player_all:
            players.append((player.name, player.name), )
        f = StartGame(players)
        context = {'form': f}
        return render(request, 'saki/start_game.html', context)
    else:
        global game_oj
        game_oj = Game(game_type=request.POST['game_type'],
                       east=Player.objects.get(name=request.POST['east']),
                       south=Player.objects.get(name=request.POST['south']),
                       west=Player.objects.get(name=request.POST['west']),
                       north=Player.objects.get(name=request.POST['north']),
                       )
        game_oj.save()
        url = reverse("saki:enter_kyoku", kwargs={'kyoku': 1, 'honba': 0})
        return HttpResponseRedirect(url)


def enter_kyoku(request, kyoku, honba):
    players = [
        (game_oj.east.name, game_oj.east.name),
        (game_oj.south.name, game_oj.south.name),
        (game_oj.west.name, game_oj.west.name),
        (game_oj.north.name, game_oj.north.name),
    ]

    if request.method == "POST":
        # kyoku_oj = Kyoku.objects.update_or_create(game=game_oj,
        #                                           kyoku=kyoku,
        #                                           honba=honba,
        #                                           riichi_bou=riichi_bou,
        #                                           agari_type=request.POST["agari_type"]
        #                                           )
        pass
    # kyoku = Kyoku.objects.all()[0]
    # print(kyoku.agari_type)

    # To Do
    # request.POST に child_point あるか check
    # if not 'child_point' in request.POST.keys():
    #   render index(request)

    # print(request.POST['child_point'])

    f_ron = RonForm(players)
    f_tsumo = TsumoForm(players)
    f_ryukyoku = RyukyokuForm()

    context = {
        'game_Object': game_oj,
        'kyoku': kyoku,
        'honba': honba,
        'riichi_bou': riichi_bou,
        'form_Ron': f_ron,
        'form_Tsumo': f_tsumo,
        'form_Ryukyoku': f_ryukyoku
    }

    # game = Game.objects.get(game_id=4)
    # tontya = game.ton

    return render(
        request,
        'saki/enter_kyoku.html',
        context
    )


def search_stats(request):
    player_all = Player.objects.all()
    player_all = [(player.name, player.name) for player in player_all]
    context = {'form': SearchStatsForm(player_all)}
    return render(
        request,
        'saki/search_stats.html',
        context
    )


def show_stats(request):
    player_name = request.POST.get('target_player', None)

    context = calc_stats(player_name)
    return render(
        request,
        'saki/stats.html',
        context
    )

from django.shortcuts import render
from django.http import Http404
from saki.forms import StartGame
from .models import Player, Game, Kyoku

from .forms import EnterKyoku, RonForm, TsumoForm


def index(request):
    return render(request, 'saki/index.html')


def start_game(request):
    f = StartGame()
    return render(request, 'saki/start_game.html', {'form': f})


def enter_kyoku_result(request):
    #if request.method == 'GET':
        #raise Http404("Question does not exist")

    f_enter_kyoku = EnterKyoku()
    f_ron = RonForm()
    f_tsumo = TsumoForm()

    # game = Game.objects.get(game_id=4)
    # tontya = game.ton
    return render(
        request,
        'saki/enter_kyoku_result.html',
        {
         'form_EnterKyoku': f_enter_kyoku,
         'form_Ron': f_ron,
         'form_Tsumo': f_tsumo
         }
    )

from django.shortcuts import render
from django.http import Http404
from saki.forms import StartGame
from .models import Player, Game, Kyoku

from .forms import EnterHand


def index(request):
    return render(request, 'saki/index.html')


def start_game(request):
    f = StartGame()
    return render(request, 'saki/start_game.html', {'form': f})


def enter_hand_result(request):
    # if request.method == 'GET':
    #     raise Http404("Question does not exist")

    f = EnterHand()
    return render(request, 'saki/enter_hand_result.html', {'form': f})

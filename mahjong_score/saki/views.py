from django.shortcuts import render
from django.http import Http404
from .models import Player, Game, Kyoku

from .forms import EnterHand


def index(request):
    return render(request, 'saki/index.html')


def enter_hand_result(request):
    #if request.method == 'GET':
        #raise Http404("Question does not exist")

    f = EnterHand()
    return render(request, 'saki/enter_hand_result.html', {'form': f})

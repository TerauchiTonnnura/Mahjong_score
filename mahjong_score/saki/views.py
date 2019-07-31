from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import StartGame, ComeBackForm
from .models import Player, Game, Kyoku, KyokuPlayer
from .mahjong_function import calc_stats, calc_kyoku, calc_honba

from .forms import RonForm, TsumoForm, RyukyokuForm, SearchStatsForm


def home(request):
    return render(request, 'saki/home.html')


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
        raise Http404


def comeback(request):
    if request.method == "POST":
        print(request.POST)
        game = Game.objects.get(id=request.POST["game_id"])
        kyoku = Kyoku.objects.filter(game=game).order_by('-id').first()
        print(kyoku)
    game_all = Game.objects.all()
    games = []
    for game in game_all:
        games.append((game.id, str(game)))
    f = ComeBackForm(games)
    context = {'form': f}
    return render(request, 'saki/comeback.html', context)


def enter_kyoku(request):
    if request.method == "GET":  # GET アクセスさせない
        raise Http404

    if "game_type" in request.POST:  # start_game からの画面遷移
        game_oj = Game.objects.create(game_type=request.POST['game_type'],
                                      east=Player.objects.get(name=request.POST['east']),
                                      south=Player.objects.get(name=request.POST['south']),
                                      west=Player.objects.get(name=request.POST['west']),
                                      north=Player.objects.get(name=request.POST['north']),
                                      )

        kyoku_oj = Kyoku.objects.create(game=game_oj,
                                                  kyoku=1,
                                                  honba=0,
                                                  riichi_bou=0,
                                                  )

        print(kyoku_oj.game)

        players = [
            (game_oj.east.name, game_oj.east.name),
            (game_oj.south.name, game_oj.south.name),
            (game_oj.west.name, game_oj.west.name),
            (game_oj.north.name, game_oj.north.name),
        ]

        f_ron = RonForm(players)
        f_tsumo = TsumoForm(players)
        f_ryukyoku = RyukyokuForm()

        context = {
            'game_Object': game_oj,
            'kyoku_Object': kyoku_oj,
            'kyoku': 1,
            'honba': 0,
            'riichi_bou': 0,
            'form_Ron': f_ron,
            'form_Tsumo': f_tsumo,
            'form_Ryukyoku': f_ryukyoku
        }

        return render(request, 'saki/enter_kyoku.html', context)

    else:
        game_id = request.POST["game_id"]
        game_oj = Game.objects.get(id=game_id)

        players = [
            (game_oj.east.name, game_oj.east.name),
            (game_oj.south.name, game_oj.south.name),
            (game_oj.west.name, game_oj.west.name),
            (game_oj.north.name, game_oj.north.name),
        ]

        kyoku = int(request.POST["kyoku"])
        honba = int(request.POST["honba"])
        riichi_bou = int(request.POST["riichi_bou"])

        kyoku_oj = Kyoku.objects.get(id=request.POST["kyoku_id"])
        kyoku_oj.riichi_bou = riichi_bou
        kyoku_oj.agari_type = request.POST["agari_type"]

        east_player_oj = Player.objects.get(name=game_oj.east.name)
        south_player_oj = Player.objects.get(name=game_oj.south.name)
        west_player_oj = Player.objects.get(name=game_oj.west.name)
        north_player_oj = Player.objects.get(name=game_oj.north.name)

        kaze_name = ['東', '南', '西', '北']

        east_oj = KyokuPlayer.objects.update_or_create(kyoku=kyoku_oj,
                                                       player=east_player_oj,
                                                       jikaze=kaze_name[(kyoku-1) % 4]
                                                       )

        south_oj = KyokuPlayer.objects.update_or_create(kyoku=kyoku_oj,
                                                        player=south_player_oj,
                                                        jikaze=kaze_name[kyoku % 4]
                                                        )

        west_oj = KyokuPlayer.objects.update_or_create(kyoku=kyoku_oj,
                                                       player=west_player_oj,
                                                       jikaze=kaze_name[(kyoku+1) % 4]
                                                       )

        north_oj = KyokuPlayer.objects.update_or_create(kyoku=kyoku_oj,
                                                        player=north_player_oj,
                                                        jikaze=kaze_name[(kyoku+2) % 4]
                                                        )

        f_ron = RonForm(players)
        f_tsumo = TsumoForm(players)
        f_ryukyoku = RyukyokuForm()

        players_oj_list = [east_oj, south_oj, west_oj, north_oj]

        # 適宜処理が必要です．
        riichi_bou = 0

        kyoku_oj = Kyoku.objects.create(game=game_oj,
                                        kyoku=calc_kyoku(kyoku, players_oj_list),
                                        honba=calc_honba(kyoku, players_oj_list),
                                        riichi_bou=riichi_bou,
                                        )

        context = {
            'game_Object': game_oj,
            'kyoku_Object': kyoku_oj,
            'kyoku': kyoku,
            'honba': honba,
            'riichi_bou': riichi_bou,
            'form_Ron': f_ron,
            'form_Tsumo': f_tsumo,
            'form_Ryukyoku': f_ryukyoku
        }

        return render(request, 'saki/enter_kyoku.html', context)


def search_stats(request):
    player_all = Player.objects.all()
    player_all = [(player.name, player.name) for player in player_all]
    context = {'form': SearchStatsForm(player_all)}
    return render(request, 'saki/search_stats.html', context)


def show_stats(request):
    player_name = request.POST.get('target_player', None)

    context = calc_stats(player_name)
    if not context:
        return HttpResponse("Error: search failed. There is no data of that person.")
    return render(request, 'saki/stats.html', context)

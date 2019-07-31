from django.db.models import Q
from .models import KyokuPlayer, Game


def calc_stats(player_name):
    kyoku_player_objects = KyokuPlayer.objects.filter(player__name=player_name)
    if not kyoku_player_objects:
        return None
    game_objects = Game.objects.filter(Q(east__name=player_name) |
                                       Q(south__name=player_name) |
                                       Q(west__name=player_name) |
                                       Q(north__name=player_name)
                                       )

    total_point = sum([dat.point_change for dat in kyoku_player_objects]) / 100.0
    game_num = len(game_objects)
    average_point = total_point / float(game_num)
    kyoku_num = len(kyoku_player_objects)
    juni_count = [0] * 4
    total_juni = 0

    for game in game_objects:
        juni_sorted = judge_juni(game)
        juni = [i for i, p in enumerate(juni_sorted) if p[0].name == player_name][0] + 1
        juni_count[juni - 1] += 1
        total_juni += juni

    agari_count = len(kyoku_player_objects.filter(agari=True))
    houju_count = len(kyoku_player_objects.filter(houju=True))

    return {'player_name': player_name,
            'total_score': total_point,
            'average_score': average_point,
            'game_num': game_num,
            'kyoku_num': kyoku_num,
            'average_juni': total_juni / float(game_num),
            'agari_rate': (agari_count / float(kyoku_num)) * 100,
            'houju_rate': (houju_count / float(kyoku_num)) * 100,
            'rate_1st': juni_count[0] / float(game_num) * 100,
            'rate_2nd': juni_count[1] / float(game_num) * 100,
            'rate_3rd': juni_count[2] / float(game_num) * 100,
            'rate_4th': juni_count[3] / float(game_num) * 100
            }


def judge_juni(game):
    play_result = [(game.east, game.east_point),
                   (game.south, game.south_point),
                   (game.west, game.west_point),
                   (game.north, game.north_point)]
    # 頭ハネも対応
    play_result.sort(key=lambda x: x[1], reverse=True)
    return play_result


def calc_kyoku(kyoku, players_oj_list):
    for player_oj in players_oj_list:
        print(player_oj.jikaze)
        if player_oj.jikaze == '東':
            if player_oj.agari:
                return kyoku
            elif player_oj.tempai:
                return kyoku
            else:
                return kyoku + 1


def calc_honba(honba, players_oj_list):
    children_agari_flag = False

    for player_oj in players_oj_list:
        if player_oj.agari:
            print(player_oj.jikaze)
            if player_oj.jikaze == '東':
                return honba + 1
            else:
                children_agari_flag = True

    if children_agari_flag:
        return 0
    else:
        return honba + 1

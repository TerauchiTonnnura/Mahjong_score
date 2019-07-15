# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Player, Game, Kyoku, KyokuPlayer
from .views import home
from django.http import HttpRequest
from datetime import datetime


class PlayerModelTest(TestCase):  # モデル自体の定義がなされているか検証
    def test_is_empty(self):
        saved_player = Player.objects.all()
        self.assertEqual(saved_player.count(), 0)

    def test_name(self):
        player = Player(name="山田太郎")
        self.assertEqual(str(player), "山田太郎")


class GameModelTest(TestCase):
    def test_is_empty(self):
        saved_game = Game.objects.all()
        self.assertEqual(saved_game.count(), 0)


class KyokuModelTest(TestCase):
    def test_is_empty(self):
        saved_game = Kyoku.objects.all()
        self.assertEqual(saved_game.count(), 0)


class KyokuPlayerModelTest(TestCase):
    def test_is_empty(self):
        saved_game = KyokuPlayer.objects.all()
        self.assertEqual(saved_game.count(), 0)


class SimulateGame(TestCase):  # KyokuPlayer作成までのテスト
    def make_instance(self):
        playerA = Player.objects.create(name="A")
        playerB = Player.objects.create(name="B")
        playerC = Player.objects.create(name="C")
        playerD = Player.objects.create(name="D")

        game = Game.objects.create(
            game_type="東風",
            date=datetime.now(),
            east=playerA,
            south=playerB,
            west=playerC,
            north=playerD,
            east_point=0,
            south_point=0,
            west_point=0,
            north_point=0
        )

        kyoku = Kyoku.objects.create(
            game=game,
            kyoku=1,
            honba=0,
            riichi_bou=0,
            agari_type="ロン"
        )

        kyokuplayerA = KyokuPlayer.objects.create(
            kyoku=kyoku,
            player=playerA,
            jikaze="東",
            point_change=12000,
            agari=True,
            riichi=True,
            houju=False,
            chonbo=False
        )
        self.assertEqual(str(kyokuplayerA), "Kyoku={} : player={}".format(kyoku, playerA))


class UrlResolveTests(TestCase):  # 各 URL にたどり着けるか検証
    def test_url_resolves_to_home_view(self):
        url = reverse('saki:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertEquals(view.func, index)

    def test_url_resolves_to_start_game_view(self):
        url = reverse('saki:start_game')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_to_enter_kyoku_view(self):
        playerA = Player.objects.create(name="A")
        playerB = Player.objects.create(name="B")
        playerC = Player.objects.create(name="C")
        playerD = Player.objects.create(name="D")

        Game.objects.create(
            game_type="東風",
            date=datetime.now(),
            east=playerA,
            south=playerB,
            west=playerC,
            north=playerD,
            east_point=0,
            south_point=0,
            west_point=0,
            north_point=0
        )

        url = reverse('saki:enter_kyoku', kwargs={'game_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_to_dotask_search_stats_view(self):
        url = reverse('saki:search_stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_to_show_stats_view(self):
        url = reverse('saki:show_stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class HtmlTests(TestCase):  # index が正しい HTMLを返しているか確認
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('saki/home.html')
        self.assertEqual(response.content.decode(), expected_html)

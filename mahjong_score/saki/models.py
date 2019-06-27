from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    game_type = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    # players = models.ManyToManyField(Player, blank=True)
    east = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='east')
    south = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='south')
    west = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='west')
    north = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='north')

    east_point = models.IntegerField(default=25000)
    south_point = models.IntegerField(default=25000)
    west_point = models.IntegerField(default=25000)
    north_point = models.IntegerField(default=25000)

    def __str__(self):
        print(self.date)
        print(self.east)
        print(self.west)
        return "{} : [{}, {}, {}, {}]".format(self.date, self.east.name, self.south.name, self.west.name, self.north.name)


class Kyoku(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    kyoku = models.IntegerField(default=1)  # 局
    honba = models.IntegerField(default=0)  # 本場
    riichi_bou = models.IntegerField(default=0)  # リー棒
    agari_type = models.CharField(max_length=10)
    ryukyoku_type = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return "{} : {}{}局{}本場".format(self.game, self.bakaze, self.kyoku, self.honba)

    def _get_bakaze(self):
        if self.kyoku <= 4:
            return '東'
        elif self.kyoku <= 8:
            return '南'

    @property
    def bakaze(self):
        return self._get_bakaze()


class KyokuPlayer(models.Model):
    kyoku = models.ForeignKey(Kyoku, on_delete=models.CASCADE)
    
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    jikaze = models.CharField(max_length=1)
    
    point_change = models.IntegerField(default=0)
    
    agari = models.BooleanField(default=False)
    riichi = models.BooleanField(default=False)
    tenpai = models.BooleanField(default=False)
    houju = models.BooleanField(default=False)
    chonbo = models.BooleanField(default=False)

    def __str__(self):
        return "Kyoku={} : player={}".format(self.kyoku, self.player)

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
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
    #oya = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='oya')  # 親
    kyoku = models.IntegerField(default=1)  # 局
    honba = models.IntegerField(default=0)  # 本場
    riichi_bou = models.IntegerField(default=0)  # リー棒
    bakaze = models.CharField(max_length=1)
    agari_type = models.CharField(max_length=10)
    ryukyoku_type = models.CharField(max_length=10, null=True)
    ## リー棒が出た時などに局プレイヤのテーブルを参照するなら，↓の３つはいらない(?)
    #agari_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='agari_player')  # 上がった人
    #houju_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='houju_player')  # 振り込んだ人
    #point = models.IntegerField()
    
    def __str__(self):
        return "{} : {}{}局{}本場".format(self.game, self.bakaze, self.kyoku, self.honba)


## 名前これでいいの ?
class KyokuPlayer(models.Model):
    kyoku = models.ForeignKey(Kyoku, on_delete=models.CASCADE)
    
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    # oya = models.BooleanField(default=True) # 自風でわかるか ?
    jikaze = models.CharField(max_length=1)
    
    # point_current = models.IntegerField(default=25000)
    point_change = models.IntegerField(default=0)
    
    # stats を求めるときに，このクラスだけを参照し，Kyoku クラスを参照する必要がないようにしたい．
    agari = models.BooleanField(default=False)
    riichi = models.BooleanField(default=False)
    tenpai = models.BooleanField(default=False)
    houju = models.BooleanField(default=False)
    ## naki = models.BooleanField(default=False)
    ## naki_num = modeld.IntegerField(default=0)
    
    def __str__(self):
        return "Kyoku={} : player={}".format(self.kyoku, self.player)
    
from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateTimeField(default=timezone.now)
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        lis = [p.name for p in self.players.all()]
        return "{} : [{}, {}, {}, {}]".format(self.date, lis[0], lis[1], lis[2], lis[3])


# class Hand(models.Model):
#     hand_id = models.ForeignKey(Game, on_delete=models.CASCADE)
#     parent = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)  # 親
#     nth = models.IntegerField(default=0)  # N本場
#     round_choices = ('東', '南', '西', '北')
#     round = models.CharField(max_length=1, choices=round_choices)
#     hora_choices = ('ロン', 'ツモ', '流局')
#     hora = models.CharField(max_length=2, choices=hora_choices)
#     discarder = models.ForeignKey(Player, on_delete=models.SET_NULL)
#     point = models.IntegerField()

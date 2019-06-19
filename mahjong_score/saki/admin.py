from django.contrib import admin
from .models import Player, Game, Kyoku, KyokuPlayer

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Kyoku)
admin.site.register(KyokuPlayer)

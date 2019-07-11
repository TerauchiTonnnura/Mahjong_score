from django.urls import path
from . import views

app_name = 'saki'
urlpatterns = [
    path('', views.index, name='index'),
    path('enter_kyoku/<int:game_id>', views.enter_kyoku, name='enter_kyoku'),
    path('start_game', views.start_game, name='start_game'),
    path('show_stats', views.show_stats, name='show_stats'),
    path('search_stats', views.search_stats, name='search_stats')
]

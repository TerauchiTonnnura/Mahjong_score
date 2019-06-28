from django.urls import path
from . import views

app_name = 'saki'
urlpatterns = [
    path('', views.index, name='index'),
    path('enter_kyoku/<int:kyoku>/<int:honba>', views.enter_kyoku, name='enter_kyoku'),
    path('start_game', views.start_game, name='start_game'),
]

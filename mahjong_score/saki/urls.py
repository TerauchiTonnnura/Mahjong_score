from django.urls import path
from . import views

app_name = 'saki'
urlpatterns = [
    path('', views.index, name='index'),
    path('start_game', views.start_game, name='start_game'),
    path('enter_hand', views.enter_hand_result, name='enter_hand_result'),
]

from django.urls import path
from . import views

app_name = 'saki'
urlpatterns = [
    path('', views.index, name='index'),
    path('enter_kyoku', views.enter_kyoku_result, name='enter_kyoku_result'),
    path('start_game', views.start_game, name='start_game'),
]

from django.urls import path
from . import views

app_name = 'saki'
urlpatterns = [
    path('', views.index, name='index'),
    path('enter_hand', views.enter_hand_result, name='enter_hand_result'),
]

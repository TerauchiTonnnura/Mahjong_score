from django import forms
from .models import Player

GAME_TYPE = {
    ('tonpu', '東風'),
    ('hanchan', '半荘')
}

NAME = Player.objects.values_list('name')

NAME = {
    ('0', '夏目漱石'),
    ('1', '芥川龍之介'),
    ('2', '太宰治'),
    ('3', '谷崎潤一郎'),
}


class StartGame(forms.Form):
    game_type = forms.ChoiceField(
        label='ゲーム',
        widget=forms.RadioSelect,
        choices=GAME_TYPE,
        required=True,
    )

    east = forms.ChoiceField(
        label='東',
        widget=forms.Select,
        choices=NAME,
        required=True,
    )
    south = forms.ChoiceField(
        label='南',
        widget=forms.Select,
        choices=NAME,
        required=True,
    )
    west = forms.ChoiceField(
        label='西',
        widget=forms.Select,
        choices=NAME,
        required=True,
    )
    north = forms.ChoiceField(
        label='北',
        widget=forms.Select,
        choices=NAME,
        required=True,
    )


RESULT_CHOICES = (
    ('ron', '栄(ロン)'),
    ('tsumo', '自摸(ツモ)'),
    ('ryukyoku', '流局')
)


class EnterHand(forms.Form):
    result = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RESULT_CHOICES,
        required=True,
    )

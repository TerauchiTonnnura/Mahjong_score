from django import forms
from .models


GAME_TYPE = {
    ('tonpu', '東風'),
    ('hanchan', '半荘')
}


class StartGame(forms.ModelForm):
    model =
    game_type = forms.ChoiceField(
        label='ゲーム',
        widget=forms.RadioSelect,
        choices=GAME_TYPE,
        required=True,
    )
    east = forms.CharField(

        label='東',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )
    south = forms.CharField(
        label='南',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )
    west = forms.CharField(
        label='西',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )
    north = forms.CharField(
        label='北',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )


CHILDREN_RON_POINT = (
    ('1000', ' 1,000'),
    ('1300', ' 1,300'),
    ('1600', ' 1,600'),
    ('2000', ' 2,000'),
    ('2300', ' 2,300'),
    ('2600', ' 2,600'),
    ('2900', ' 2,900'),
    ('3200', ' 3,200'),
    ('3600', ' 3,600'),
    ('3900', ' 3,900'),
    ('4500', ' 4,500'),
    ('5200', ' 5,200'),
    ('5800', ' 5,800'),
    ('6400', ' 6,400'),
    ('7100', ' 7,100'),
    ('7700', ' 7,700'),
    ('8000', ' 8,000'),
    ('12000', '12,000'),
    ('16000', '16,000'),
    ('24000', '24,000'),
    ('32000', '32,000'),
)

PARENT_RON_POINT = (
    ('1500', ' 1,500'),
    ('2000', ' 2,000'),
    ('2400', ' 2,400'),
    ('2900', ' 2,900'),
    ('3400', ' 3,400'),
    ('3900', ' 3,900'),
    ('4400', ' 4,400'),
    ('4800', ' 4,800'),
    ('5300', ' 5,300'),
    ('5800', ' 5,800'),
    ('6800', ' 6,800'),
    ('7700', ' 7,700'),
    ('8700', ' 8,700'),
    ('9600', ' 9,600'),
    ('10600', '10,600'),
    ('11600', '11,600'),
    ('12000', '12,000'),
    ('18000', '18,000'),
    ('24000', '24,000'),
    ('36000', '36,000'),
    ('48000', '48,000'),
)

CHILDREN_TSUMO_POINT = (
    ('300,500', '  300 -   500'),
    ('400,700', '  400 -   700'),
    ('400,800', '  400 -   800'),
    ('500,1000', '  500 -  1,000'),
    ('600,1200', '  600 -  1,200'),
    ('700,1300', '  700 -  1,300'),
    ('800,1500', '  800 -  1,500'),
    ('800,1600', '  800 -  1,600'),
    ('900,1800', '  900 -  1,800'),
    ('1000,2000', ' 1,000 -  2,000'),
    ('1200,2300', ' 1,200 -  2,300'),
    ('1300,2600', ' 1,300 -  2,600'),
    ('1500,2900', ' 1,500 -  2,900'),
    ('1600,3200', ' 1,600 -  3,200'),
    ('1800,3600', ' 1,800 -  3,600'),
    ('2000,3900', ' 2,000 -  3,900'),
    ('2000,4000', ' 2,000 -  4,000'),
    ('3000,6000', ' 3,000 -  6,000'),
    ('4000,8000', ' 4,000 -  8,000'),
    ('6000,12000', ' 6,000 - 12,000'),
    ('8000,16000', ' 8,000 - 16,000'),
)

PARENT_TSUMO_POINT = (
    ('500', '  500'),
    ('700', '  700'),
    ('800', '  800'),
    ('1000', ' 1,000'),
    ('1200', ' 1,200'),
    ('1300', ' 1,300'),
    ('1500', ' 1,500'),
    ('1600', ' 1,600'),
    ('1800', ' 1,800'),
    ('2000', ' 2,000'),
    ('2300', ' 2,300'),
    ('2600', ' 2,600'),
    ('2900', ' 2,900'),
    ('3200', ' 3,200'),
    ('3600', ' 3,600'),
    ('3900', ' 3,900'),
    ('4000', ' 4,000'),
    ('6000', ' 6,000'),
    ('8000', ' 8,000'),
    ('12000', '12,000'),
    ('16000', '16,000'),
)

UNIQUE_RYUKYOKU_TYPE = (
    ('0', '荒牌平局'),
    ('1', '四風連打'),
    ('2', '九種九牌'),
    ('3', '四開槓'),
    ('4', '三家和'),
    ('5', '四家立直'),
)


class RonForm(forms.Form):
    child_point = forms.ChoiceField(
        label='子のロン上がり',
        widget=forms.Select,
        choices=CHILDREN_RON_POINT
    )

    parent_point = forms.ChoiceField(
        label='親のロン上がり',
        widget=forms.Select,
        choices=PARENT_RON_POINT
    )


class TsumoForm(forms.Form):
    child_point = forms.ChoiceField(
        label='子のツモ上がり',
        widget=forms.Select,
        choices=CHILDREN_TSUMO_POINT
    )

    parent_point = forms.ChoiceField(
        label='親のツモ上がり',
        widget=forms.Select,
        choices=PARENT_TSUMO_POINT
    )


class RyukyokuForm(forms.Form):
    unique = forms.ChoiceField(
        widget=forms.Select,
        choices=UNIQUE_RYUKYOKU_TYPE
    )

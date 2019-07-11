from django import forms
from .resources import (GAME_TYPE, UNIQUE_RYUKYOKU_TYPE,
                        CHILDREN_TSUMO_POINT, CHILDREN_RON_POINT,
                        PARENT_TSUMO_POINT, PARENT_RON_POINT)


class StartGame(forms.Form):
    def __init__(self, players, *args, **kwargs):
        super(StartGame, self).__init__(*args, **kwargs)
        self.fields['east'].choices = players
        self.fields['south'].choices = players
        self.fields['west'].choices = players
        self.fields['north'].choices = players
        
    game_type = forms.ChoiceField(
        label='ゲーム',
        widget=forms.RadioSelect,
        choices=GAME_TYPE,
        required=True,
    )

    east = forms.ChoiceField(
        label='東',
        widget=forms.Select,
        choices=(),
        required=True,
    )
    south = forms.ChoiceField(
        label='南',
        widget=forms.Select,
        choices=(),
        required=True,
    )
    west = forms.ChoiceField(
        label='西',
        widget=forms.Select,
        choices=(),
        required=True,
    )
    north = forms.ChoiceField(
        label='北',
        widget=forms.Select,
        choices=(),
        required=True,
    )


class RonForm(forms.Form):
    def __init__(self, players, *args, **kwargs):
        super(RonForm, self).__init__(*args, **kwargs)
        self.fields['houju_player'].choices = players
        self.fields['agari_player'].choices = players

    houju_player = forms.ChoiceField(
        label='放銃プレイヤー',
        widget=forms.Select,
        choices=()
    )

    agari_player = forms.ChoiceField(
        label='あがりプレイヤー',
        widget=forms.Select,
        choices=()
    )

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
    def __init__(self, players, *args, **kwargs):
        super(TsumoForm, self).__init__(*args, **kwargs)
        self.fields['agari_player'].choices = players

    agari_player = forms.ChoiceField(
        label='あがりプレイヤー',
        widget=forms.Select,
        choices=()
    )

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


class SearchStatsForm(forms.Form):
    def __init__(self, players, *args, **kwargs):
        super(SearchStatsForm, self).__init__(*args, **kwargs)
        self.fields['target_player'].choices = players

    target_player = forms.ChoiceField(
        label='プレイヤ',
        widget=forms.Select,
        choices=(),
        required=True
    )

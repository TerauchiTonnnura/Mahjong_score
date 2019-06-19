from django import forms


GAME_TYPE = {
    ('tonpu', '東風'),
    ('hanchan', '半荘')
}


class StartGame(forms.Form):
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

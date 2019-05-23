from django import forms


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
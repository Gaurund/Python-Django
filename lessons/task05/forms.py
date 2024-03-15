from django import forms


class GameForm(forms.Form):
    choice = forms.ChoiceField(
        choices=[
            ('C', 'Coin'),
            ('D', 'Dice'),
            ('R', 'Random number')
        ],
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-input'}
        )
    )
    tries = forms.IntegerField(max_value=64)

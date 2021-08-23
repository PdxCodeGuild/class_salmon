from django import forms
from pokemon.models import Pokemon

class CaughtForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "caught_by"
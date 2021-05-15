from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label="Item name", max_length=200)
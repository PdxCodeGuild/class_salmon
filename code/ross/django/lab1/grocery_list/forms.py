# from django import forms
from django.forms import ModelForm
from .models import GroceryItem

class ItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = '__all__'
from django.contrib import admin
from .models import GroceryItem #import your classes(models) from the models.py file here

# Register your models here.
admin.site.register(GroceryItem)#run a function for each model
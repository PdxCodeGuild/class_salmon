from django.contrib import admin
from .models import Links

# Connect to models.py and grab the links model.
admin.site.register(Links)

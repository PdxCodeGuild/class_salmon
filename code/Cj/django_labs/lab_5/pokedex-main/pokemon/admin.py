from django.contrib import admin

from .models import Pokemon, SoundEffect, Type

admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(SoundEffect)

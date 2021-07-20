from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.register(Question)#run a function for each model
admin.site.register(Choice)

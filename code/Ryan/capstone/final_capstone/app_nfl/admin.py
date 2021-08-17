from django.contrib import admin
from .models import Team, Schedule

# class TeamAdmin(Team):
#     model = Team
#     list_display = ["Team"]#,"Schedule"]
#     list_display.sort(reverse=True)

admin.site.register(Team)
admin.site.register(Schedule)

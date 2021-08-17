from django.db import models
from app_users.models import CustomUser
from app_nfl.models import Team

class Square(models.Model):
    team_x = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='TeamX')
    team_y = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='TeamY')
    boardStatus = models.BooleanField(default=False)

    def __str__(self):
        return f"team_x vs team_y"

class Cell(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    cellStatus = models.BooleanField(default=False)
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.user

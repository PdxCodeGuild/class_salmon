from django.db import models

class Square(models.Model):
    team_x = models.CharField(max_length=200)
    team_y = models.CharField(max_length=200)
    boardStatus = models.BooleanField(default=False)

class Cell(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    cellStatus = models.BooleanField(default=False)
    user = models.OneToOneField()

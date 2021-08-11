from django.db import models

class Schedule(models.Model):
    date = models.DateTimeField()
    homeTeam = models.ForeignKey(Team)
    awayTeam = models.ForeignKey(Team)

class Team(models.Model):
    teamName = models.CharField(max_length=100)
    logo = models.ImageField()
    win = models.IntegerField()
    loss = models.IntegerField()
    draw = models.IntegerField()

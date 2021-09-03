from django.db import models


# Create your models here.
class Students(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    fav_topic = models.CharField(max_length=100)
    fav_teach = models.CharField(max_length=100)
    capstone_url = models.URLField()

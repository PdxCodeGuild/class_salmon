from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    fav_topic = models.CharField(max_length=200)
    fav_teacher = models.CharField(max_length=200)
    capstone = models.URLField()

    def __str__(self):
        return self.fname + " | " + self.lname

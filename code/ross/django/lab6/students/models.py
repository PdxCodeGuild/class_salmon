from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    cohort = models.CharField(max_length=20)
    favorite_topic = models.CharField(max_length=20)
    favorite_teacher = models.CharField(max_length=20)
    capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.firstname
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    cohort = models.CharField(max_length=40)
    favorite_topic = models.CharField(max_length=40)
    favorite_teacher = models.CharField(max_length=40)
    capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.last_name
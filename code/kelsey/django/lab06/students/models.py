from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=100)
    favorite_topic = models.CharField(max_length=100)
    favorite_teacher = models.CharField(max_length=100)
    capstone = models.URLField()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
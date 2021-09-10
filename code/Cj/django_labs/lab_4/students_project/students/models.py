from django.db import models
from django.db.models.fields import CharField, URLField

class Students(models.Model):
    first_name = CharField(max_length=50)
    last_name =CharField(max_length=50)
    cohort = CharField(max_length=200)
    favorite_topic = CharField(max_length=200)
    favorite_teacher = CharField(max_length=50)
    capstone = URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        
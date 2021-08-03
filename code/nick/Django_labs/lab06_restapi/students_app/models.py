from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    cohort = models.CharField(max_length=6)#call corhorts by year and two digit number
    favorite_topic = models.CharField(max_length=120)
    favorite_teacher = models.CharField(max_length=120)
    capstone_url = models.CharField(max_length=70)#or use models.URLField() if you feel like it..........

    def __str__(self):
        return self.first_name
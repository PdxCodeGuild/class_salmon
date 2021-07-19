from django.db import models

class Cello(models.Model):
    name = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=128)
    price = models.FloatField()
    string_count = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.manufacturer}'
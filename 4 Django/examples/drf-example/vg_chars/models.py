from django.db import models

class Franchise(models.Model):
    name = models.CharField(max_length=128)
    developer = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}: {self.developer}'

class Character(models.Model):
    name = models.CharField(max_length=128)
    origin_story = models.TextField(null=True, blank=True)
    first_appeared = models.DateField()

    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return f'{self.name}: {self.franchise}'
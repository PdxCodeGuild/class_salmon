from django.db import models

class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True, default='anything')
    
    def __str__(self):
        return self.short_url
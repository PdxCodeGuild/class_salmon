from django.db import models

class Links(models.Model):

    # Store the long URL
    original_url = models.URLField()

    # Store the short URL
    short_url = models.CharField(max_length=15)

    def __str__(self):
        return self.short_url

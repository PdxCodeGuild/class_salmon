from django.db import models

class Links(models.Model):

    # Store the long URL
    url = models.URLField()

    # Store the short URL
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.code

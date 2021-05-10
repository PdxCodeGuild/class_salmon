from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

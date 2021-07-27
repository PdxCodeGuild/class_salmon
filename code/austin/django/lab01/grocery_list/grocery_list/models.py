import datetime
from django.db import models

# Create your models here.
#text description created date completed date completed boolean
class GroceryItem(models.Model):
    item_text = models.CharField(max_length=50)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
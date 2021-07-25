import datetime
from django.db import models
from django.utils import timezone

class Item(models.Model):

    # Text Description
    item_text = models.CharField(max_length=200)

    # Created date
    created_date = models.DateTimeField()

    # Completed Date
    completed_date = models.DateTimeField(null=True, blank=True)

    # Completed
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text

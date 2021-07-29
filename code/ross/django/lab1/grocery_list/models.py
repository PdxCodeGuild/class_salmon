from django.db import models
# from django.db.models import Model
from django.utils import timezone
from django.conf import settings

class GroceryItem(models.Model):
    description = models.CharField(max_length=40)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
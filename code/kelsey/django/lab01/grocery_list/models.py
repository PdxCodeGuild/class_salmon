from django.conf import settings
from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
from django.conf import settings
from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    # completed = 
    
    def __str__(self):
        return self.text
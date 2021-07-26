from django.db import models
from django.utils import timezone
from django.conf import settings

class GroceryItem(models.Model):
    description = models.CharField(max_length=40)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = False

    def newItem(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description
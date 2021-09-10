from django.db import models

# Create your models here.
class Grocery(models.Model):
    item_text = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    purchased = models.BooleanField()

    def __str__(self):
        return self.item_text
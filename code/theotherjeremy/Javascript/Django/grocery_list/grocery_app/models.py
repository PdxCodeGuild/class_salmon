from django.db import models
from django.utils import timezone
# Create your models here.
# You can think of a model in the database as a spreadsheet
#  with columns (fields) and rows (data).


class GroceryItem(models.Model):
    item_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(auto_now=True)
    done_box = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text

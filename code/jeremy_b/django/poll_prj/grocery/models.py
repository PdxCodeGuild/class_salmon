from django.db import models
from django.utils import timezone

import datetime

class List(models.Model):
    list_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # determine when list was created.
    def created_recently(self, days):
        return timezone.now() >= self.create_date >= timezone.now() - datetime.timedelta(days=days)

    def is_list_active(self):
        return self.is_active

    def __str__(self):
        return self.list_name


class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    list_item_text = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)

    def is_item_complete(self):
        return self.is_complete

    def __str__(self):
        return self.list_item_text


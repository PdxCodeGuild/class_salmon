from django.db import models

# Create your models here.
# You can think of a model in the database as a spreadsheet
#  with columns (fields) and rows (data).


class Shortness(models.Model):
    # these are querysets. refer to them in html by {{item_text}}

    long_url = models.URLField(max_length=300)
    short_url = models.CharField(max_length=50)

    def __str__(self):
        return self.long_url

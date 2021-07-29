from django.db import models
from django.utils import timezone

# Create your models here.
class SubmittedUrl(models.Model):
    url_description = models.CharField(max_length=200)#basically a character field is a string with a maximum length
    create_date = models.DateTimeField(default=timezone.now())#publication date allows for ordering, latest items first, etc.
    code_for_url = models.CharField(max_length=8, default='')
    # completed_date = models.DateTimeField(null=True, blank=True)
    # is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.code_for_url


# class CodedUrl(models.Model):
#     code_description = models.
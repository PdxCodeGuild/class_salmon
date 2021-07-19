import random
import string

from django.db import models

CODE_CHARACTERS = string.ascii_letters + string.digits


class URL(models.Model):
    long_url = models.URLField()
    code = models.CharField(max_length=7, primary_key=True, editable=False)

    def generate_code(self):
        self.code = ''.join([random.choice(CODE_CHARACTERS) for _ in range(7)])


class Click(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    http_referer = models.URLField(null=True, blank=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='clicks')

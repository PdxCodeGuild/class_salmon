from django.db import models
from requests import request

class UrlShortener(models.Model):
    long_url = models.URLField()
    short_url = models.URLField()
    url_name = models.CharField(max_length=50)
    short_code = models.CharField(max_length=50, unique=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_code


class ClickData(models.Model):
    # Store data related to the clicks here.  You never know when it might come in handy for ad revenue...
    related_url = models.ForeignKey(UrlShortener, on_delete=models.PROTECT)
    ip_addr = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    click_date = models.DateTimeField(auto_now_add=True)

    # return the click data as a dictionary.
    def __str__(self):
        return {'related_url': self.related_url, 'ip_addr': self.ip_addr, 'host': self.host, 'total_clicks': self.total_clicks, 'click_date': self.click_date}




from django.db import models
from django.contrib.auth import get_user_model

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.URLField()
    image_back = models.URLField()
    caught_by = models.ManyToManyField(get_user_model(), related_name='caught')
    gif = models.ImageField(null=True, blank=True, upload_to='animated/')
    cry = models.FileField(null=True, blank=True, upload_to='cries/')
    # types = the set of Types associated with that Pokemon

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')
    type_tag = models.ImageField(null=True, blank=True, upload_to='type_tags/')

    def __str__(self):
        return self.type
    
class SoundEffect(models.Model):
    media = models.FileField(null=True, blank=True, upload_to='sound_effects/')

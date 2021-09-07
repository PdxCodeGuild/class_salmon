from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
# from pokemon.models import Pokemon

class CustomUser(AbstractUser):
    pass
    # caught = the set of Pokemon associated with that user
    # caught = models.ManyToManyField(Pokemon)
    # This is where you would add additional fields.
    # These will be in the DB alongside username, email, etc



    def __str__(self):
        return self.username

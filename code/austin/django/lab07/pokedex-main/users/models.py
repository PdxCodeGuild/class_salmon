from django.db import models
from django.contrib.auth.models import AbstractUser
from pokemon.models import Pokemon

class CustomUser(AbstractUser):
    pokemon_caught = models.ManyToManyField(Pokemon, related_name="caught_by_user")

    # This is where you would add additional fields.
    # These will be in the DB alongside username, email, etc

    def __str__(self):
        return self.username

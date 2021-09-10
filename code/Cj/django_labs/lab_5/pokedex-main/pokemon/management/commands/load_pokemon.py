import json
import os

from django.core.management.base import BaseCommand

from ...models import Pokemon, Type

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # Clear existing Pokemon and Types
        Pokemon.objects.all().delete()
        Type.objects.all().delete()

        # Open Pokemon JSON and load to list of dictionaries
        with open('pokemon.json') as p:
            pokemon_list = json.loads(p.read())
        
        # Loop through Pokemon to add to DB
        # folder_path = 'C:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\cj\\django_labs\\lab_5\\pokedex-main\\static\\animated'
        # gif_list = []
        # for file_name in os.listdir(folder_path):
        #     gif_list.append(file_name)
        # gif_list= sorted(gif_list, key=len)
        # i = 0
        for pokemon in pokemon_list['pokemon']:

            # Convert units to m and kg
            pokemon['height'] /= 10
            pokemon['weight'] /= 10

            # Add Pokemon to DB
            poke_obj = Pokemon.objects.create(
                number=pokemon['number'],
                name=pokemon['name'],
                height=pokemon['height'],
                weight=pokemon['weight'],
                image_front=pokemon['image_front'],
                image_back=pokemon['image_back'],
                gif = f"animated/{pokemon['number']}.gif",
                cry = f"cries/{pokemon['number']}.ogg"
            )
            # i += 1
            # Loop through types list
            # For each type, create type if it doesn't exist yet, than add that type to current Pokemon
            for type in pokemon['types']:
                # type_obj, created = Type.objects.get_or_create(type=type)
                type_obj, created = Type.objects.get_or_create(type=type, type_tag=f"type_tags/{type}.png")
                type_obj.pokemon.add(poke_obj)

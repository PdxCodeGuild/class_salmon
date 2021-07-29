from django.conf import settings
from random import choice
from string import ascii_letters, digits

available_chars= ascii_letters + digits
def create_shortener(available_chars):
    return "".join([choice(available_chars) for char in range (10)])
print(create_shortener)


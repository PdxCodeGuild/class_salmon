# Pokedex Starter

## Installation

Make sure you have Python and Pipenv installed on your computer.

Download the repo and save it to your code folder in the class repo. *make sure you download it, don't clone it or it won't upload to the class repo correctly*

If you are not running Python 3.8, edit the last line of the `Pipfile` to refer to your version instead.

Navigate to the pokedex folder in the terminal and do the following:

- `pipenv install` Create the virtual enviroment and install dependencies.
- `pipenv shell` Enter the new virtual enviroment.
- `python manage.py migrate users` Migrate the user model. *this django project uses a custom user model, you MUST migrate the users app before migrating the rest!*
- `python manage.py migrate` Migrate all other models.
- `python manage.py createsuperuser` Create yourself a super user.
- `python manage.py load_pokemon` Load Pokemon into the database.

You're good to go! This Django project comes with a database full of Pokemon, login/logout/registration pages, and a `home.html` template for you to create your Vue app.

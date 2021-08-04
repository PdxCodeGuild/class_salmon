# Lab 07 - Pokedex with Django REST Framework and Vue

I built a Django app. It's got a basic user framework with a custom user model, `Pokemon` and `Type` models, and a database full of Pokemon. Let's build it an API, and then use that API to build a single page Vue application.

## Part 1 - Setup

You can find the app to download here: https://github.com/flamingveggies/pokedex *make sure you download it, don't clone it*

Follow the instructions to install and set up the starter project. It has some things you haven't seen like custom management commands and a custom user model, so there are a few extra steps. Make sure you follow the instructions!

## Part 2 - Basic API

Create an API for the Pokedex in Django Rest Framework. Your API needs to have endpoints for all the Pokemon, as well as some sort of nested serializers so that your API returns the names of the types that each Pokemon belongs to, not just the pk of those types.

Use the [WSVincent DRF tutorial](https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api) and the in-class examples as references.

## Part 3 - Vue Frontend

Build a Vue frontend for our Pokedex! I already provided you with a `home.html` template you can use. Make sure to leave the links to the login/logout/signup pages so that a user can get themselves authenticated (otherwise the API won't work!).

Your frontend should display a list of Pokemon upon loading.

[DRF and Vue](https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/docs/DRF%20and%20Vue.md)  
[Axios](https://github.com/axios/axios)

## Part 4 - More Features

You must implement ONE of the following features into your app. You can implement more if you'd like.

### Edit Pokedex

Add the ability to create new Pokemon, update the stats of existing Pokemon, and delete Pokemon. Make sure that only registered users can edit your list of Pokemon. You are not required to implement the ability to add types to newly created Pokemon, but it's good practice.

### User Lists

Add a list to your Pokedex of all Pokemon that a logged in user has caught. Add the ability to mark a pokemon as caught or remove a marked pokemon from the caught list.

The models are already set up to do this. `Pokemon` has a many-to-many relationship with `CustomUser`. You will also need API endpoints for the users. To add a Pokemon to a user's list, add the pk of that Pokemon to the `caught` array and send a `PUT`/`PATCH` request with the new array of caught Pokemon. To remove a Pokemon from a user's list, remove the pk of that Pokemon from the `caught` array and send a `PUT`/`PATCH` request with the new array of caught Pokemon.

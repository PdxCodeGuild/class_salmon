# Lab 06 - Django REST Framework and Vue

I built a Django app. It's got a basic user framework, a model, and a database full of data. Let's build it an API, and then use that API to build a single page Vue application.

## Part 1

You can find the app to download here: https://github.com/flamingveggies/drf-example *make sure you download it, don't clone it*

Use the [WSVincent DRF tutorial](https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api) as a reference. Build an API using the instructions. Notice how little code it takes it build a full API with Django REST Framework! Once you have the API built, use the built in API documentation website provided by DRF to explore your API and get a sense for the API calls you'll need to make from the frontend.

## Part 2

Build a Vue frontend for our students! I already provided you with a `home.html` template you can use. Make sure to leave the links to the login/logout/signup pages so that a user can get themselves authenticated (otherwise the API won't work!).

Your frontend should display a list of students upon loading. It should also offer the ability to create new students in the database.

[DRF and Vue](https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/docs/DRF%20and%20Vue.md)  
[Axios](https://github.com/axios/axios)

## Part 3 (Optional, but good capstone practice)

Add student update and delete functionality to your Vue application.

## Part 4 (Optional)

Use the following tutorial to dive deeper into the components of Django Rest Framework:

[Official Django REST Framework Tutorial - A Beginners Guide](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)


# How to start a Django project &nbsp;(_PDXCG Style_)

Open a terminal and go to wherever you want to create your project!

Make sure to replace **$PROJECT_NAME** with your own project name. Your project name should be named in  snake_case and contain no captial letters.

This will also require `pipenv` to be installed!

## Setup the project

1. Create a directory
    * `mkdir $PROJECT_NAME`
2. Change into that directory 
    * `cd $PROJECT_NAME`
3. Install django
    * `pipenv install django`
4. Get into the environment
    * `pipenv shell`
5. Create your project in the currect directory
    * `django-admin startproject $PROJECT_NAME .`
    * **The period at the end of this command is important!** It says ignore creating a new folder and put the contents of our new project in the current directory. 

   
   
## Create an app

Creating an app to add to your project is done by calling `python manage.py startapp <app_name>`

Django won't recognize your app until you append it to `INSTALLED_APPS` list in `settings.py`.
eg:
```python
INSTALLED_APPS = [
   ... other apps
   '<app_name>',  
]
```

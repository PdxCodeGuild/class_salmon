
# How to start a Django project &nbsp;(_PDXCG Style_)

## Table of Contents

1. [Setup the project](#setup)
    - [Reference: "Am I inside or outside the virtual environment?"](#where-am-i)
1. [Create a Django App](#create-app)
1. [Create a View](#create-view)
1. [Create a Route to the View](#create-route)
1. [Running the web server locally](#runserver)
1. [Create Models](#create-models)
1. [Add the Model to the Admin Panel](#add-model)
1. [Create a Template](#create-template)
1. [Render a Template](#render-template)
1. [Set up template directories](#template-dirs)
1. [Set up static directories](#static-dirs)

- ## [Quickstart (Abbreviated version)](#quickstart)

---
## Setup the project <a name="setup"></a>

1. Create a directory. Open a terminal and navigate to a new (blank) folder, and  create your project folder. Make sure to replace **$PROJECT_NAME** with your own project name. Your project name should be named in snake_case and contain no capital letters.
    * `mkdir $PROJECT_NAME`
2. Change into that directory 
    * `cd $PROJECT_NAME`
3. Install django (requires `pipenv` to be installed via `pip install pipenv` . In case you ever need to remove the virtual environment, use `pipenv --rm`)
    * `pipenv install django`
4. Get into the environment
    * `pipenv shell`
    * `pip list` (verify Django is installed)
5. Create your project in the currect directory
    * `django-admin startproject $PROJECT_NAME .`
    * **The period at the end of this command is important!** It says ignore creating a new folder and put the contents of our new project in the current directory. 


### How to tell, "Where am I?" "Inside the virtual environment or not?" <a name="where-am-i"></a>

There are several ways to check whethe you are inside the virtual environment or not:

* `pipenv shell` (You can't shell into the environment again if you're already in there. But do NOT created a doubly-nested virtual environment!)
* `pip list` (Should show a full list of installed python packages on your system, or a more limited list inside the virtual environment.)
* `which python` (Does not work on all OS/python/terminal configurations.) This should give two possibilities. `C/system/python` would mean you are outside in your main terminal, or something including `C/users/name/.virtualenvs/$PROJECT-NAME-{UNIQUE-PIPENV-CODE}/Scripts/python` Both the `.virtualenvs` and the `unique-project-name-with-code` indicate you are inside the virtual environment.



---   
## Create a Django app inside the project <a name="create-app"></a>

Creating an app to add to your project is done by calling `python manage.py startapp $APPNAME_HERE`

Django won't recognize your app until you append it to the `INSTALLED_APPS` list in `settings.py`.

eg:
```python
INSTALLED_APPS = [
   ... other apps
   '$APPNAME_HERE',  
]
```

---
## Create a View <a name="create-view"></a>

- In your app's `views.py`:
```python
from django.http import HttpResponse
def <viewname>(request):
    return HttpResponse('ok')
```
A common `<viewname>` is `index`.

---
## Create a Route to the View <a name="create-route"></a>

- Create a `urls.py` inside your app
- Add a route in your app's `urls.py` which points to the the view
- Add an `app_name` to be able to look up paths when you render a template

```python
from django.urls import path
from . import views

app_name = '<app name>' # for namespacing
urlpatterns = [
    path('<path>', views.<viewname>, name='<viewname>')
]
```

- Add a route in your project's `urls.py` which points to the app's `urls.py` using `include`

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<path>/', include('<appname>.urls')) # Note: all your app urls will start with this path
]
```
---
## Running the web server locally <a name="runserver"></a>

At this point, you should run the server (`python manage.py runserver`) and go to `localhost:8000/app_path/view_path` and verify that you can access the view.
The local Django web server will generally remain running and automatically restart if it detects changes in any .py files, but this is the first place you should check if you can't access it locally. Close the server like any python file with `Cmd+C / Control+C`. Remember to restart it after performing any direct commands to the manage.py file. 

---
## Create Models <a name="create-models"></a>

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- (optional) View the SQL commands that will occur during migrations: `python manage.py sqlmigrate <appname> <migration number>`. You can find the migration number and the code that'll be executed during the migration in `<appname>/migrations/<migration number>_initial.py`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

---
## Add the Model to the Admin Panel <a name="add-model"></a>

- Add a `def __str__(self):` to your model so the admin interface knows how to display it.
- Make your app visible in the admin panel by registering your models with our app's `admin.py`
    ```py
    admin.site.register(Model)
    ```

```python
from django.contrib import admin
from .models import <model name 1> <model name 2>
admin.site.register(<model name 1>)
admin.site.register(<model name 2>)
```

- Go to `localhost:8000/admin` in your browser, and add some data.

---
## Create a Template <a name="create-template"></a>

- Create a folder inside your app called `templates`, inside of that create another folder with the name of your app, and inside of *that* create a `<filename>.html`. You can view examples of the template syntax [here](03%20-%20Templates.md).

---
## Render a Template <a name="render-template"></a>

- Inside your view, you can use the `render` shortcut to render a template. The first parameter is the request, the second parameter is the name of the template, and the third is a dictionary containing the values you'd like to render in the template.

```python
from django.shortcuts import render
def <view name>(request):
    context = {<name-value pairs>}
    return render(request, '<app name>/<template name>.html', context)
```

---
### Set up template directories <a name="template-dirs"></a>
In `settings.py`:
```py
TEMPLATES = [
    {
		...
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		...
	}
]
```

---
### Set up static directories <a name="static-dirs"></a>
In `settings.py`
```py
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),    
)
```

---
---
# Quickstart (Abbreviated version) <a name="quickstart"></a>
## Create the Project

- Create a site/project: `django-admin startproject $PROJECT_NAME`
- Move into the site's directory: `cd $PROJECT_NAME`
- Run migrations to create the database and user system `python manage.py migrate`
- Create an admin account with `python manage.py createsuperuser`, and enter a username, email address, and password

## Create the App

- Create an app: `python manage.py startapp $PROJECT_NAME`
- Add your app (`PROJECT_NAME.apps.PROJECT_NAMEConfig`) to the `INSTALLED_APPS` list [] in `settings.py`
	- Note: PROJECT_NAMEConfig is found in your `appname/apps.py` file


---
---

### *Note: the following "virtualenv / venv" commands are deprecated, but the old instructions may be useful in rare situations:*

## Set up Virtual Environment
If you haven't install `virtualenv`, do so now:
```
> [sudo] pip install virtualenv
```

Create a new project directory where you want to store your project and `cd` into it:
```
> mkdir project_dir_name
> cd project_dir_name
```

Create a new virtual environment:
```
> virtualenv ENV
```

To enter your virtual environment: 
In Linux/OSX:
```
> source ENV/bin/activate
```

In Windows:
```
> ENV/Scripts/activate
```

You are now in your virtual environment! This is a clean state with only Python and Pip installed. Install all the dependencies for your project inside this environment. 

For this course, install Django 2.0.0 
```
> pip install django==2.0.0
```

(Optional) To export your packages:
```
> pip freeze > requirements.txt
```

To exit your virtual environment:
```
> deactivate
```
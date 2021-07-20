# Django Quickstart
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

## Create a Project and App

- Create a site/project: `django-admin startproject <site/project name>`
- Move into the site's directory: `cd <site/project name>`
- Run migrations to create the database and user system `python manage.py migrate`
- Create an admin account with `python manage.py createsuperuser`, and enter a username, email address, and password

## Create an App

- Create an app: `python manage.py startapp <app-name>`
- Add your app (`appname.apps.AppnameConfig`) to the `INSTALLED_APPS` in `settings.py`
	- Note: AppnameConfig is found in your `appname/apps.py` file

## Create a View

- In your app's `views.py`:
```python
from django.http import HttpResponse
def <viewname>(request):
    return HttpResponse('ok')
```

## Create a Route to the View

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

At this point, you should run the server (`python manage.py runserver`) and go to `localhost:8000/app_path/view_path` and verify that you can access the view.

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- (optional) View the SQL commands that will occur during migrations: `python manage.py sqlmigrate <appname> <migration number>`. You can find the migration number and the code that'll be executed during the migration in `<appname>/migrations/<migration number>_initial.py`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

## Add the Model to the Admin Panel

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


## Create a Template

- Create a folder inside your app called `templates`, inside of that create another folder with the name of your app, and inside of *that* create a `<filename>.html`. You can view examples of the template syntax [here](03%20-%20Templates.md).

## Render a Template

- Inside your view, you can use the `render` shortcut to render a template. The first parameter is the request, the second parameter is the name of the template, and the third is a dictionary containing the values you'd like to render in the template.

```python
from django.shortcuts import render
def <view name>(request):
    context = {<name-value pairs>}
    return render(request, '<app name>/<template name>.html', context)
```

### Set up template directories
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

### Set up static directories
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

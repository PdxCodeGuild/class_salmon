# Django and Vue

So you want to use Django as your backend, but you want more interactivity on your pages than you can provide with Django templates? Good news -- Django and Vue play very nicely together, and are easy to integrate. There's just a few things to keep in mind.

## Import Vue

To use Vue in a Django template, simply make sure the end of your `body` has a `script` tag to load Vue. I recommend writing your Vue app in a `script` tag at the bottom of your template instead of an external JavaScript file. This can make it easy to have your Django app pass data into your Vue app, like the CSRF token or even a context object. Even if you're using Django Rest Framework, it means all your templates are in the same file.

```django
{% extends 'base.html' %}

{% block content %}

<div id="app">
  <p>{{ message }}</p> # Uh oh, this is the same template syntax as Django! We'll need to fix that...
</div>
<script src="https://unpkg.com/vue"></script>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      message: 'Hello world!',
    },
    methods: {
      logMessage: function () {
        console.log(this);
      }
    },
    mounted: function () {
      logMessage();
    }
  });
</script>

{% endblock %}
```

## Changing delimiters

By default, both Django and Vue templates use `{{ }}` to insert expressions. We need to change the delimiters that Vue uses to square brackets instead. This can be done by adding a `delimiters` value to our root Vue configuration object.

```django
{% extends 'base.html' %}

{% block content %}

<div id="app">
  <p>[[ message ]]</p> # Much better!
</div>
<script src="https://unpkg.com/vue"></script>
<script>
  let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], // This is new
    data: {
      message: 'Hello world!',
    },
    methods: {
      logMessage: function () {
        console.log(this);
      }
    },
    mounted: function () {
      logMessage();
    }
  });
</script>

{% endblock %}
```

## Passing data context from Django to Vue

We now have a working Vue app in a Django template! How to we transfer over the data from our backend? We have two options:

  - Pass data from our Django view to our context and then load our template context into our Vue instance (this is clunky and we're not going to do it)
  - If we have an API (this could be manually programmed Django views that return JSON or a full-fledged Django REST Framework app) we can use the `mounted` method on out root Vue component to fetch the data needed to initialize our page. To do this you need to build a REST API, but can then build a more modern and robust application.
  
Let's look at how to do both!

### Clunky -- Passing context to Javascript

This requires modifying our Django view a little bit. Our context needs to include JSON data that our JavaScript code can read. Remember, a Django QuerySet is a Python object, JSON is a text string that JavaScript can parse into a data object.

We need to use something called a *serializer* to go through our QuerySet object and turn it into JSON. Luckly, Python has one built in. We then need to pass this JSON data into our context so that we can access it in our template. In the following example I'm using a functional view so I've added it to my context object. If you're using a class-based view, you can use `get_context_data` to add extra content to your context.

#### views.py
```python
...
incomplete_items = serializers.serialize('json', GroceryItem.objects.filter(is_completed=False).order_by('-date_created'))
complete_items = serializers.serialize('json', GroceryItem.objects.filter(is_completed=True).order_by('-date_completed'))
...
context = {
  'incomplete_items': incomplete_items,
  'complete_items': complete_items,
  ...
  }
...
```

Now we need to load our JSON into JavaScript. Django 2.2 adds a very handy new template tag called `json_script` that takes an object in context (it won't work with a standard QuerySet!) and creates a `<script>` tag containing the JSON code. We can then use `JSON.parse()` to load it as a normal JavaScript variable.

The syntax for `json_script` is `{{ <value containing JSON>|json_script:"<id of script tag to create>" }}`

At this point we have our data in JavaScript, and can initialize our Vue instance using our new JavaScript variables.

#### template.html
```django
...
<script src="https://unpkg.com/vue"></script>
{{ complete_items|json_script:"init-complete" }}
{{ incomplete_items|json_script:"init-incomplete" }}
<script>
  let json_incomplete_items = JSON.parse(JSON.parse(document.getElementById('init-incomplete').textContent));
  let json_complete_items = JSON.parse(JSON.parse(document.getElementById('init-complete').textContent));
  let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'], // This is new
    data: {
        incomplete_items: json_incomplete_items,
        complete_items: json_complete_items,
        message: "Hello World!"
    },
    methods: {
      logMessage: function () {
        console.log(this);
      }
    },
    mounted: function () {
      logMessage();
    }
  });
</script>
...
```

### Better -- `mounted` API call

If you have an API, you can avoid all the awkward conversions we just did. You can just use Django to load your Vue app, and then use an `axios` Ajax call in your `mounted` method to load the initial data when the page loads.

This requires you to have an API to get the data from. You have two choices: create manual API endpoints by creating views that return a `JSONResponse` (see *02 - Views.md*), or use Django Rest Framework to quickly create a full API, and then call the endpoint that corresponds the data you would like to load.

Once you have an API endpoint, your code is the same as any other API call. Make sure you either include the CSRF token or set your API views to be `csrf_exempt`.

```django
...
  mounted: {
    let crsf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    axios({
      url: '/api/grocery_item/',
      method: 'get',
      headers: {
        'X-CSRFToken': csrf_token
      }
    }).then(res => this.grocery_items = res.data)
  }
...
```

## Sending information back to Django

You'll need to send a data object back to your API. Axios makes this easy. Again, this can be a custom API endpoint you created (see *02 - Views.md*) or it can be a Django Rest Framework endpoint.

#### template.html
```django
...
  methods:
    save: {
      let crsf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
      axios({
        url: 'api/grocery_item/',
        method: 'post',
        headers: {
          X-CSRFToken: csrf_token
        },
        data: this.new_grocery_item
      }).then(res => console.log(res))
    },
...
```

If you're using Django REST Framework, that's it! If it didn't work, read your own API documentation and the DRF documentation to make sure you are submitting properly.

If you're using a custom API endpoint that you wrote, make sure it connects to a view. You can read the JSON body of your incoming request using `request.body` and parsing back from JSON to a Python dictionary.

#### views.py
```python
def save(request):
  if request.method == 'POST':
    json_data = json.loads(request.body)
    try:
      # access data here. you probably want to get an object, edit it, and save it.
    except KeyError:
      HttpResponseServerError("Malformed data!")
    HttpResponse("Thumbs up, you did it!")
```

## Templates vs Vue

Vue and Django templates fulfill the same role: presentation of data. With this in mind, decide which you are going to use to render your page. For instance, trying to use `{% for %}` and `v-for` in the same template will quickly make things complicated and buggy.

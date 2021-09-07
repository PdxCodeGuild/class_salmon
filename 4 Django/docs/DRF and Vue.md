# Django Rest Framework and Vue

Once you have an API made in Django Rest Framework, it's easy to retrieve data using Vue.

## Two ways to structure your project

In most professional web applications, the front end and the back end are completely separate code bases. Often they are even in different repositories! This gives you the advantage of modular development. It's easy for one person or team to work on the front end while others work on the back end, with a common API interface between them. This also means you can swap out front-ends or the back-end serving your API as technologies come and go. It also makes it easy to have multiple front-ends, for example iOS/Android apps, a desktop app, a web app, etc.

There is a downside though. Because the back-end and front-end are separate, authentication is a lot more work. In vanilla Django, cookies and user sessions are used to track when a user is logged in as they visit templates. By hosting our front-end separately, Django can't manage users for us. Instead, we need to use something called token authentication. When a user wants to log in to our app, they need to send an API request with their authentication details. If they are correct, DRF will return an authentication token to be submitted with all other API requests.

For our purposes, we're going to bypass this requirement by serving up a hybrid approach to DRF and Vue. By embedding our Vue app in a Django template, we can take advantage of Django's user session system an we will not have to write any special authentication code beyond what we did in vanilla Django. This approach creates code that can sometimes get messy and inelegant whith a larger Vue application, but it saves us a lot of time and hassle.

## Import Vue

To use Vue in a Django template, simply make sure the end of your `body` has a `script` tag to load Vue. I recommend writing your Vue app in a `script` tag at the bottom of your template instead of an external JavaScript file. This means all your templates are in the same file.

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

## Call your API

If you have an API, you can  use an `axios` ajax call in your `mounted` method to load the initial data when the page loads.

This requires you to have an API to get the data from. You have two choices: create manual API endpoints by creating views that return a `JSONResponse` (see *02 - Views.md*), or use Django Rest Framework to quickly create a full API, and then call the endpoint that corresponds the data you would like to load.

Once you have an API endpoint, your code is the same as any other API call. Make sure you either include the CSRF token in the template or set your API views to be `csrf_exempt`.

```django
...
  data: {
    grocery_items: [],
    new_grocery_item: {
      name: "",
    },
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

```django
...
  data: {
    grocery_items: [ ... ],
    new_grocery_item: {
      name: " ... ",
    },
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

This is a *create* example, hence the `method: 'post'`. To *edit*, use `method: 'put'` or `method: 'patch'`. To *delete*, use `method: 'delete'`. For more information, take a look at the DRF's browsable API to see what your endpoints and avaliable methods are. If you submit an invalid request, DRF is very good and letting you know why. You can either handle the error in your Axios promise, or simply open the browser development tools and open the `Network` tab to view the error message that DRF returned.

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

Vue and Django templates fulfill the same role: presentation of data. With this in mind, decide which you are going to use to render your page. For instance, trying to use `{% for %}` and `v-for` in the same template will quickly make things complicated and buggy. For best results, I recommend using Vue to create pages and avoiding Django, even though technically you're editing a Django template.

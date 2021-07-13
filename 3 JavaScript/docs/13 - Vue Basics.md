# Vue

Vue is a JavaScript framework for building user interfaces. Vue is a MVVM framework (Model View View-model). This is a fancy
way of saying that you give Vue a JavaScript object that represents the state (or data, or model) of your application and a
template (or view) of the visual representation of your data. Vue provides a view-model that binds your data to your template
and syncs them to each other instantly as both update. This means that as the user updates the values of elements on the page
they are instantly reflected in the data object, and as you update the data object with event listeners or other methods the
webpage template is instantly re-rendered with the new data. This removes the need to do manual DOM manipluation, making it
easy to write more complicated user interfaces and interactive web pages.

For more information about JavaScript frameworks and why to use them, go [here](https://www.academind.com/learn/javascript/jquery-future-angular-react-vue/).

More detailed explanations and code examples can be found in the Vue guide [here](https://vuejs.org/v2/guide/).

A YouTube series on Vue basics can be found [here](https://www.youtube.com/watch?v=5LYrN_cAJoA&list=PL4cUxeGkcC9gQcYgjhBoeQH7wiAyZNrYa) and the solution repo [here](https://github.com/iamshaunjp/vuejs-playlist/tree/lesson-1).

## Installing

Vue can be run from a CLI tool and it's own project like Django, but in class we will be running Vue from a CDN, loaded
in with a `script` tag. This means we can add Vue to an existing HTML page and add Vue functionality and features
at our own page, on top of our existing front-end knowledge.

`<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`

Also highly recommended:
* [Vuetur syntax highlighting and snippits for VS Code](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
* [Vue devtools for Chrome/Firefox/etc](https://github.com/vuejs/vue-devtools)

## Declarative Rendering

```
<div id="app">
  {{ message }}
</div>
```

```
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

Looks a lot like Django, doesn't it? We instantiate a `new` Vue instance, and pass it a configuration object. `el` represents
the CSS selector of the element to create our Vue app inside. `data` is our model or state, kind of like the context in Django.
When the value of `message` changes, our page will automatically change to match.

We can also use a *directive* called `v-bind` to bind attribute values to Vue's data model.

```
<div id="app-2">
  <span v-bind:title="message">
    Hover your mouse over me for a few seconds
    to see my dynamically bound title!
  </span>
</div>
```

```
var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})
```

## Loops and Conditionals

```
<div id="app-3">
  <span v-if="seen">Now you see me</span>
</div>
```

```
var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  }
})
```

```
<div id="app-4">
  <ol>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ol>
</div>
```

```
var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue' },
      { text: 'Build something awesome' }
    ]
  }
})
```

Again, this should feel familiar. Instead of using template tags, we're using *directives* that look like HTML attributes.
Note that unlike with templte tags, the directives go directly on the HTML elements.

## Events and Input

```
<div id="app-5">
  <p>{{ message }}</p>
  <button v-on:click="reverseMessage">Reverse Message</button>
</div>
```

```
var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

We can also give Vue as many *methods* as we want, which we can call in our template with the `v-on:<event_name>` directive.
Finally, we can use the `v-model` directive to bind the value of an input element to our data model.

```
<div id="app-6">
  <p>{{ message }}</p>
  <input v-model="message">
</div>
```

```
var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Hello Vue!'
  }
})
```

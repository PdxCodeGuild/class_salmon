# Lab 11: Vue Todos

Use Vue to create a simple todo list in the browser.

Your Vue app will need to do a few things:
 * Store an array of objects (the todos themselves)
 * List each todo
 * Allow the user to add and remove todos
 * Allow a user to toggle if a task is complete or not
 
 Reference the Vue.js [Introduction Guide](https://vuejs.org/v2/guide/).

## How to get started

* Create a simple local HTML project with the following structure:
```
todos
├── css
│   └── site.css
├── index.html
└── js
    └── site.js`
```

## How to serve your application

* Install this plug-in for VSCode: `https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer`
* Make sure VSCode is open to the same folder as your `index.html`
* On the bottom bar in VSCode you should see an icon that says `Go Live`
* Click it and you're serving up a local version of your html file. It also auto-reloads everytime you make a change, neat right?

## How to structure your `index.html`

Example: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Todo List</title>
    <!-- Add your styles here! -->
    <link rel="stylesheet" href="/css/site.css" />
</head>
<body>
    <div id="app">
        {{ message }}
    </div>

    <!-- Include Vue from a CDN of your choice, I chose unpkg -->
    <script src="https://unpkg.com/vue"></script>
    <!-- Include your code here... -->
    <script src="/js/site.js"></script>
</body>
</html>
```

### How to start a simple Vue app:
```js
new Vue({
    el: '#app',
    data: {
        message: 'Hello world!'
    }
})
```

**Now if you check your browser you should see the message `Hello world!`**
**That means everything is working**

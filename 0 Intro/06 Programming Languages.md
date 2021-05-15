

# Software

- [Hardware and Machine Code](#hardware-and-machine-code)
- [Low- and High-Level Languages](#low--and-high-level-languages)
- [Types of Languages](#types-of-languages)
  - [Programming Languages](#programming-languages)
  - [Non-Programming Languages](#non-programming-languages)
  - [Imperative vs Declarative](#imperative-vs-declarative)
  - [Procedural vs Object-Oriented](#procedural-vs-object-oriented)
- [Typing Systems](#typing-systems)

## Hardware and Machine Code

The earliest computers were merely mechanical calculators, which could take numbers as input and perform arithmetic operations on them. Soon those operations were made more open-ended, giving rise to "code" and "software". On modern computers, all code is ultimately run by the CPU as **machine code** or **assembly language**. Statements in assembly are terse and minimalist, consisting of statements like "move these bytes from main memory to a register" and "add the bytes in register 1 and register 2, and store the result in register 3". There are no functions, no objects, and no classes. An executable file (.exe) contains machine code. When it's run, the operating system loads that machine code into memory and begins executing it, statement by statement.

## Low- and High-Level Languages

Writing anything in machine code is extremely tedious and it's easy to make mistakes, so we developed higher level languages that could be translated into a low level language that could be run directly by the CPU. We can write code in a high-level language like C++ and then run a program called a **compiler** to compile the code into an executable, which can then be shared and run directly.

High-level languages make code easier to write and understand, and can represent a bridge between the software developer and the hardware. The also often have features like **garbage collection** which clears un-used data in memory automatically. Memory leaks are a constant issue in languages without garbage collection, and are one of the reasons a computer slows down if used too long without restarting.

An issue that arose with this is **portability**. There are many different types of CPUs in the world, and many different types of assembly. To distribute software widely, one must compile their code into many different executable files, and hope that their users will download and run the right one. To address this, we developed **interpreters**, which are also programs that take source code in a high-level language and execute it line-by-line. Users could then install an interpreter once and run any software given to them that's understood by the interpreter. An example of this is the python interactive interpreter, which one can access by running "python" in a command-line. Languages like Java, Python, and C# use both compilation and interpretation. Their source code is compiled to an intermediary language called **byte code** which is then run by the interpreter.

This doesn't mean that low-level languages are obsolete. High-level languages are easier to write and read, and enable us to more quickly develop software. However, the also restrict us with what we can do, and are less efficient than if we wrote all our code in a lower-level language. A metaphor might be using an expresso machine where you can push a single button rather than grinding and filtering the beans yourself.

- **High-Level**
- Java, Python, C#
- C++
- C
- Machine Code
- **Low-Level**

## Types of Languages


### Programming Languages

| type | language |
| ----|-----|
| Imperative and Procedural | C, C++, C#, Java, Python |
| Object-Oriented | C++, C#, Java, Python |
| Functional | Haskell, Lisp & Scheme, Scala, Python |
| Declarative | Prolog |


### Non-Programming Languages

| type | language |
| ----|-----|
| Data Formatting|  JSON, XML|
| Markup | HTML, MD|
| Style | CSS|
| Query | SQL, GraphQL, OCL, LINQ |


- [List of Programming Languages by Type](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
- [Esoteric Programming Languages](https://en.wikipedia.org/wiki/Esoteric_programming_language)

### Imperative vs Declarative

In imperative languages, statements are executed line-by-line which perform operations on variables. In declarative languages, one defines relationships between variables. If the following code were in an imperative language, `y` would be 10. If it was in a declarative language, `y` would be 20, as the second line defines a relationship, not an operation to be performed.

```
x = 5
y = 2*x
x = 10
print(y)
```

### Procedural vs Object-Oriented





## Typing Systems

One dichotomy in typing systems is between **static** and **dynamic** typing. With static typing systems, variables are always of a particular type and cannot change type. Functions also specify the types of their parameters and return values. With dynamic typing, variables can change types and functions can take parameters of any type. Dynamic typing is also called "duck typing"- if it looks like a duck and sounds like a duck, it's a duck. This means that methods on objects aren't checked until the code attempts to access them.

Static typing systems are more rigid, but the prevent more errors and can give more meaningful error messages, like "you passed this function a variable of the wrong type". Dynamic typing is more flexible, but are more prone to errors and error messages are more ambiguous. For example, if you pass a variable to a function of the wrong type, it won't crash until it's inside the function, when it goes to access a method or perform an operation on the variable.

```python
x = 5
x = 5.6

def add(a, b):
  return a + b
print(add(5, 2)) # 7
print(add('hello', ' world!')) # hello world!

def lower_and_split(s):
  return s.lower().split()
print(lower_and_split('Hello World!')) # ['hello', 'world!']
print(lower_and_split(5)) # crash
```

```java
int x = 5 // the type of the variable is defined
x = 5.6 // crash

// the type of the parameters and return value are defined
int add(int a, int b) {
  return a + b
}
System.out.println(add(5, 2)) // 7
System.out.println(add('hello', ' world!')) // crash
```

Another dichotomy in typing systems is between **weak** and **strong** typing. Strong typing means that every variable has a definite type at any time, even if that type might change. Weak typing means that the type is ambiguous. JavaScript is considered "weakly typed" because of **type coersion**. If one compares variables of different types, JavaScript will attempt to convert them to the same type to properly compare them.

```javascript
let x = 5
let y = '5'
if (x == y) {
  console.log('??')
}
```

|               | Static Typing | Dynamic Typing |
| --------------| --------------| ---------------|
| Strong Typing | Java          | Python         |
| Weak Typing   | -            | JavaScript     |

## Libraries and Frameworks


### Python


#### Common Built-in Modules

- math: additional math functions like cos, sin, 
- decimal: more advanced floating point arithmetic
- random: generate random numbers
- datetime, time, calendar: working with dates and times
- re: regular expressions
- os, os.path: file operations
- itertools, functools: advanced operations on iterables and functions
- collections: data structures
- csv: csv file parsing


#### Common Non-Built-in Modules

These can be installed using `pip install <module>`.

- [Pillow](https://python-pillow.org/): image manipulation
- [Requests](http://requests.readthedocs.io/en/master/): http requests
- [Twisted](http://twistedmatrix.com/trac/): networking engine
- [Scrapy](https://scrapy.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): web scraping
- [nltk](http://www.nltk.org/): natural language processing
- [NumPy](http://www.numpy.org/): advanced mathematics
- [SciPy](https://www.scipy.org/): scientific computing
- [PyGame](http://www.pygame.org/news.html): game framework
- [matplotlib](http://matplotlib.org/): 2D/3D plotting
- [TkInter](https://wiki.python.org/moin/TkInter), [wxPython](https://www.wxpython.org/), [PyQT](https://sourceforge.net/projects/pyqt/), [PyGTK](https://wiki.python.org/moin/PyGtk): GUI

#### Links to sites with lists of fun python libraries

Wow there are so many awesome libraries for python you can integrate into your projects!
- [Here's](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/) some.
- [Here's](https://tryolabs.com/blog/2017/12/19/top-10-python-libraries-of-2017/) some more.
- Oh dang! [Here's](http://www.pythonforbeginners.com/api/list-of-python-apis) even more!

### Django

[django packages](https://djangopackages.org/)


### Front-End

You can view a list [here](https://www.keycdn.com/blog/front-end-frameworks/).

#### CSS

CSS frameworks can be used to make your site look pretty quickly and easily. Each framework has its own style and number of features. You can view a long list [here](https://github.com/troxler/awesome-css-frameworks).

- [Bootstrap](http://getbootstrap.com/), [w3schools tutorial](https://www.w3schools.com/bootstrap4/default.asp)
- [Materialize](http://materializecss.com/)
- [Pure.css](https://purecss.io/)
- [Foundation](http://foundation.zurb.com/sites/docs/)
- [Skeleton](http://getskeleton.com/)
- [Material Design](https://material.io/guidelines/#)
- [Kube](https://imperavi.com/kube/)
- [Milligram](http://milligram.io/)
- [Bulma](http://bulma.io/)
- [Vuetify](https://vuetifyjs.com/) (for use with Vue.js)
- [Material UI](http://www.material-ui.com/#/) (for use with React)
- [fontawesome.com](https://fontawesome.com/) (icons)

#### JavaScript Frameworks

You can view a long list on [wikipedia](https://en.wikipedia.org/wiki/List_of_JavaScript_libraries), [javascripting.com](https://www.javascripting.com/), and [here](https://github.com/collections/front-end-javascript-frameworks).

##### General UI

- [AngularJS](https://angularjs.org/)
- [Angular](https://angular.io/)
- [React](https://facebook.github.io/react/)
- [Vue.js](https://vuejs.org/)
- [Ember.js](https://www.emberjs.com/)
- [Riot.js](http://riotjs.com/)

##### Data Visualization

- [D3](https://d3js.org/)
- [Chart.js](http://www.chartjs.org/)
- [Dygraph](http://dygraphs.com/)
- [Vega](https://vega.github.io/vega/)


##### Music / Sound

- [Tone.js](https://tonejs.github.io/)
- [Howler.js](https://howlerjs.com/)
- [Sound.js](https://createjs.com/soundjs)


##### 3D Graphics

- [three.js](https://threejs.org/)
- [A-Frame](https://aframe.io/)
- [wrld](https://www.wrld3d.com/)

##### Games

- [Phaser](https://phaser.io/)
- [Babylon.js](http://www.babylonjs.com/)


### Public APIs

You can view long lists of public APIs [here](https://github.com/toddmotto/public-apis), [here](https://github.com/abhishekbanthia/Public-APIs), and [here](https://apilist.fun/). [Here's](http://www.pythonforbeginners.com/api/list-of-python-apis) a few more!

- Users
    - [randomuser.me](https://randomuser.me/documentation)
    - [reques.in](https://reqres.in/)
    - [jsonplaceholder](https://jsonplaceholder.typicode.com/)
- Weather: [openweathermap.org](http://openweathermap.org/api)
- Number Facts: [numbersapi.com](http://numbersapi.com/#42)
- Photos: [flickr.com](https://www.flickr.com/services/api/) (requires key)
- Astronomical Data: [api.nasa.gov](https://api.nasa.gov/#live_example)
- USA Population Data: [datausa.io](https://datausa.io/about/api/)


# Classes

- [Introductory Example](#introductory-example)
- [Inheritance](#inheritance)
- [ES5 Example](#es5-example)

## Introductory Example

JavaScript does not have true classes like Python. It uses something called prototypal inheritance. This means that instead of objects being unique instances of classes, objects can have prototype objects that they inherit from. However, ES6 introduced a much easier way of writing "classes" in JavaScript. They still rely on prototypal inheritance under the hood, but we can now use a syntax that looks more familiar.

Below is an example comparing the use of a class to that of an object. The object behaves similarly, except you'll have to re-write the entire structure every time you create an instance. Also, each instance will have its own copy of the `get_balance` function, resulting in greater memory overhead.

```javascript
// using a class
class ATM {
    constructor(balance=0) {
      this.balance = balance
    }
    get_balance() {
      return this.balance
    }
}

let atm = new ATM(5.0)
alert(atm.get_balance())

// using an object
let atm = {
  balance: 5.0,
  get_balance: function() {
    return this.balance
  }
}

alert(atm.get_balance())
```

## Inheritance

```javascript
class Animal {
    constructor(legs = 0) {
        this.legs = legs
    }

    move() {
        if (this.legs > 0) {
            console.log('walk')
        } else {
            console.log('slither')
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs) // invoke the parent class's constructor
        this.sound = sound
    }

    bark() {
        console.log(this.sound)
    }
    
    move() { // override the parent method
      super.move() // call the parent method (optional)
      console.log('dog moving')
    }
}

let myDog = new Dog(4)

console.log(myDog.legs) // logs 4
myDog.move() // logs 'walk', 'dog moving'
myDog.bark() // logs 'ruff'
```


## ES5 Example

The other way to create objects in JavaScript is to use the prototype system directly. This is more complicated and much more awkward, but you will see it often in the wild, so it's knowing and recognizing.

```javascript
function Animal(legs) {
    this.legs = legs || 0 // use default value if needed
}

Animal.prototype.move = function () {
    if (this.legs > 0) {
        console.log('walk')
    } else {
        console.log('slither')
    }
}

function Dog(legs, sound) {
    Animal.call(this, legs) // parent 'constructor'
    this.sound = sound || 'ruff'
}

Dog.prototype = Object.create(Animal.prototype)

Dog.prototype.bark = function () {
    console.log(this.sound)
}

var myDog = new Dog(4)

console.log(myDog.legs) // logs 4
myDog.move() // logs 'walk'
myDog.bark() // logs 'ruff'
```


# Data Structures and Abstract Data Types

There are several ways to store structured data in a Python program. (For way more detail than I go into here, read up on [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) in the official Python docs.)

## List

Lists are known as “arrays” in most other languages. A list is a simple *ordered* container for other values.

Example:

```py
supercar_makes = ['McLaren', 'Bugatti', 'Maserati', 'Lamborghini', 'Ferrari', 'Aston Martin']
    
mixed_data = ['a string', 42, {'a':'dictionary'}]
```

To access a member of a list, you reference its index. This makes it convenient to loop over the values. _Note that these indexes start at 0, not 1!_

Example:

```py
supercar_makes[2] #> 'Maserati'
    
for i in range(0, len(supercar_makes)):
    print(supercar_makes[i])
```

Despite their simplicity and because they guarantee order, lists have many uses including acting as [queues](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) and [stacks](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).

## Tuple

Tuples are immutable lists. The syntax to create them is similar (you use parentheses instead of square brackets) as is the syntax to access members.

Example:

```py
my_siblings = ('Mike', 'Sue', 'Kim')
my_siblings[2] #> 'Kim'
```

## Dict

Called “associative arrays” in some other languages, dictionaries in Python allow you to store arbitrary data, indexed by keys. These are super efficient at retrieving values.

Example:

```py
food_ratings = {'burrito':9.5, 'pizza':7.0, 'curry':8.0, 'liverwurst':-472.9}
    
character = {'name':'Brienne of Tarth', 'role': 'knight', 'kings_killed': 1, 'allegiances': ['House Tarth', 'House Baratheon', 'Renly Baratheon’s Kingsguard', 'House Tully', 'House Stark']}
```

You can access members (values) of the dictionary directly using ‘sub’ syntax.

Example:

```py
food_ratings['curry']  # > 8.0
```

If you want to iterate over the values in a dictionary, you must first retrieve the keys using the built-in `.keys()` method.

Example:

```py
for key in character.keys():
    print(character[key])
```

Note that the results are not guaranteed to be in any particular order!

## Set

A set is an unordered collection of data with no duplicate elements.

Example:

```py
fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(fruits) #> {'pear', 'banana', 'orange', 'apple'}

letters_in_mississippi = set('mississippi')
print(letters_in_mississippi) #> {'m', 'p', 's', 'i'}

letters_in_missouri = set('missouri')
print(letters_in_missouri) #> {'r', 'i', 'u', 'o', 'm', 's'}

# sets enable set operations such as intersection, union, etc.
print(letters_in_mississippi - letters_in_missouri) #> {'p'}
print(letters_in_mississippi | letters_in_missouri) #> {'r', 'i', 'u', 'o', 'm', 'p', 's'}
print(letters_in_mississippi & letters_in_missouri) #> {'m', 's', 'i'}
print(letters_in_mississippi ^ letters_in_missouri) #> {'r', 'u', 'o', 'p'}
```

Accessing members of a set is a bit clunky. First, you need to cast the set as a list.

Example:

```py
list_of_letters_in_mississippi = list(letters_in_mississippi)
print(list_of_letters_in_mississippi) #> ['m', 'p', 's', 'i']
```

## Stack

A stack is a collection of nodes with operations occuring at one end only. Think of a real-world stack of plates - plates can only be taken from or added to the top of the pile in a Last In First Out (LIFO) operation. We both *push* and *pop* items at the tail.

Simple Python stack implementation (uses lists):
```py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

# Alternatively, you can just implement a stack using a list and only appending to and popping from it.

stack = []
stack.append(1)
print(stack)  # > [1]
stack.append(2)
print(stack)  # > [1,2]
stack.append(3)
print(stack)  # > [1,2,3]
stack.pop()
print(stack)  # > [1,2]
stack.pop()   
print(stack)  # > [1]
```

Stacks are handy for remembering states (e.g. undo/redo).

## Queue

A queue is an ordered collection of nodes with operations that run in a First In First Out (FIFO) policy. Think of a real-world queue or line - the first person in gets served. We *enqueue* at the tail and *dequeue* at the head.

Simple Python queue implementation (uses lists):
```py
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

# Alternatively, you can just implement a queue using a list and only appending to end and popping from the front.

queue = []
queue.append(1)
print(queue)  # > [1]
queue.append(2)
print(queue)  # > [1,2]
queue.append(3)
print(queue)  # > [1,2,3]
queue.pop(0)  # > 1
print(queue)  # > [2,3]
queue.pop(0)  # > 2 
print(queue)  # > [3]
```

Queues are useful in programming like queues are in the real world. They act as buffers that store data until they need to be used on a first come first serve FIFO basis.

Variations of the Queue data structure include **deques** (or double-ended queues), and **priority queues** (where elements of higher priority get serviced first). We won't delve much on those here, but it's well worth a read! 

It's good to understand the basics of what these data structures are and what they are good for. Knowing when and how to utilize them will help you choose the optimal data to solve your problem!

## Graph

Graphs allow for a representation of relationships between different nodes. Graphs consist of two main parts: the nodes themselves and their edges (connections representing the relationship between connected nodes) Connections can be directed (the relationship exists in only one direction) or undirected (the relationship exists in both directions).

Graphs are useful for storing relationships and paths, such as game states.


## Tree

Trees allow for a hierarchical representation of relationships between different nodes. Each node has a parent node and optional children nodes. If a node doesn't have a parent, it is the *root* node (the top of the tree). If a node doesn't have children, it is a *leaf* node.

Simple Python tree implementation
```py
class Tree:
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        child = Tree(data, parent=self)
        self.children.append(child)

# Alternatively, you can just implement a tree using Python's builtin defaultdict recursively.

from collections import defaultdict
def Tree():
    return defaultdict(Tree)

                        #                        1
tree = Tree()           #                      / | \  
tree[1][2][5][6]        #                    2   3   4  
tree[1][3] = Tree(7)    #                    |   |    /\
tree[1][4][8]           #                    5   7   8  9
tree[1][4][9][10]       #                    |          |
                        #                    6          10

# We can print out the tree as json
import json
print(json.dumps(tree)) # > {"1": {"2": {"5": 6}, "3": 7, "4": {"8": {}, "9": {}}}}
```
Here, 1 is the root node, and 6, 7, 8, and 10 are leaf nodes.

Trees are useful for representing hierarchical data and sorted data. **Binary Search Trees** are a good way of storing data in a way that makes it efficiently searchable.

Variations of the Tree data structure include **Binary Search Trees** (left-right sorted trees with at most two children, excellent for searching), **heaps** (top-down sorted trees, good for min, max), and **Red-Black Trees** (self-balancing BST). We won't delve much on those here, but it's well worth a read! 

## When should you use which type?

The following table shows some of the relative characteristics of the different types:

    | Type  | Length? | Ordered? | Lookup? | Mutable? |
    |-------|---------|----------|---------|----------|
    | List  | Yes     | Yes      | No      | Yes      |
    | Tuple | Yes     | Yes      | No      | No       |
    | Dict  | Yes     | No       | Yes     | Yes      |
    | Set   | No      | No       | No      | Yes      |

There is _no shame_ in converting between data structures within a single problem.
There is no perfect data structure that answers all of your questions, so…

## Think list when…

* You need guaranteed order
* Implementing a queue or stack
* You want to be able to count items
* “I have no idea!” — lists are a good default

## Think tuple when…

* A list would do, but you need to ensure the values don’t change once it’s created

## Think dict when…

* You want simple (fast!) lookups
* You’re mapping keys to values

## Think set when…

* You want to quickly determine whether your data contains a particular value
* You need to determine whether two sets of data contain common members
* You need to guarantee uniqueness

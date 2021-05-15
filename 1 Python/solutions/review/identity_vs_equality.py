


# identity - two variables point to the same object (id() returns the same value)

x = 'hello'
y = x
print(id(x))
print(id(y))
print(x is y)
print(x == y)

# equality - two objects have the same value

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(id(x))
print(id(y))
print(x is y)
print(x == y)





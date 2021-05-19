fruits = ["apples", "banana", "orange"]
vegetables = ["tomato", "potato", "beans"]

grocery = [fruits, vegetables]

print(grocery, fruits, vegetables)
print(grocery[0][1])

for g in grocery:
    print(g)
    for p in g:
        print(p)


def add(a, b):
    return a + b


x = add(1, 2) + 1
print(x)

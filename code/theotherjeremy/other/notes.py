
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[1] += 1

print(x)


def removal(x, val):
    return [val for val in x if val != 4]


print(removal(x, 4))

# same same but different
x[:] = (value for value in x if value != 9)
print(x)

# or
while 5 in x:
    x.remove(5)
print(x)

[i for i in x if i != 8]

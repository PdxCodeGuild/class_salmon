


def get_square_roots(x):
    return x**0.5, -x**0.5 # tuple packing

values = get_square_roots(4)
print(values)

root1, root2 = get_square_roots(4) # tuple unpacking
print(root1)
print(root2)


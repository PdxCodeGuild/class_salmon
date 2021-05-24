ticket = [11,22,33,44,55,66]

# args
def for_loop(*args):
  print(args) # args is a tuple
  for arg in args:
    print(arg)

for_loop(1,2,3,4,5,6)
for_loop(ticket)

for i in range(len(ticket)):
  print(ticket[i], i)

for i in ticket:
  print(i)

abc = ['a', 'b', 'c']
ABC = ['A', 'B', 'C']

# enumerate
for i, letter in enumerate(abc): 
  print(ABC[i], abc[i])

# tuple unpacking
def gimme_two_xs():
  return 'x', 'x'

x1, x2 = gimme_two_xs()
print(x1)
print(x2)
tup = gimme_two_xs()
x1 = tup[0]
x2 = tup[1]
print(x1)
print(x2)
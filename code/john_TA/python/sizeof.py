import sys


# midway trough page: https://stackoverflow.com/questions/1839289/why-should-functions-always-return-the-same-type 

''  # string 49!
() # tuple 40!
[] # list 56
{} # dict 64!

print(sys.getsizeof(''))
print(sys.getsizeof([]))
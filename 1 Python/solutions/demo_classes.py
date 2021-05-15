

# function vs method
# method is a special type of function

# functions
# print('hello')
# x = int('5')

# nums = [1, 2, 3]
# nums.append(4) # method



# response = requests.get('https://www.google.com/')
# print(response.text)


# this_is_snake_case - python variables, functions (methods)
# thisIsCamelCase - JavaScript/C/C#/Java
# ThisIsTitleCaseOrPascalCase - python classes
# this-is-kebab-case - css classes


from datetime import datetime
# x = int('5')
# y = str(5)
# z = datetime(2021, 4, 22)
# w = str() # invoke the initializer of the string class
# w = ''









# if __name__ == '__main__'
import math

class Point:
    def __init__(self, llama, shark): # this is the initializer
        # print(self)
        self.tapier = llama # these are member variables
        self.platypus = shark
        self.unicorn = 'hello!'
    
    def distance(self, p): # method, or 'member function'
        dx = self.tapier - p.tapier
        dy = self.platypus - p.platypus
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.tapier *= v
        self.platypus *= v
    
    def __str__(self):
        return f'({self.tapier},{self.platypus})'

    def __repr__(self):
        return f'Point({self.tapier},{self.platypus})'



# self - specified in the parameter list of each method, but it's not passed when the method is called
# 'self' is the object / class instance on which the method was called

p1 = Point(5, 2) # call the initializer, instantiate the class
print(p1.tapier) # 5
print(p1.platypus) # 2
print(p1.unicorn) # hello!
print(type(p1)) # Point
p2 = Point(8, 4)
print(p1.distance(p2)) # 'self' is p1
# print(Point.distance(p1, p2))

p1 = Point(5, 2)
p1.scale(2)
# Point.scale(p1, 2)
print(p1.tapier) # 10
print(p1.platypus) # 4
# without the __str__ this printed <__main__.Point object at 0x000002134B7ACF10>
print(p1) # (10,4)
print(repr(p1))


d = datetime.now()
print(d) # __str__ of datetime
print([d]) # __repr__ of datetime


z = eval('5 + 2*3')
print(z)


# clone an object using repr
p1_clone = eval(repr(p1))
print(p1_clone)







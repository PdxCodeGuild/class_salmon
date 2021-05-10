### Point is an example of both a class and a custom data type ###

# import math

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     name = "pretty cool point object" # static variable
    
#     def distance(self, p): # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)

#     def change_name(self, new_name): # this does nothing because name is not an instance variable
#         name = new_name
    
#     def scale(self, v):
#         self.x *= v
#         self.y *= v

#     @staticmethod
#     def from_polar(r, theta): # static methods belong to the type, not the instance
#         px = r * math.cos(theta)
#         py = r * math.sin(theta)
#         return Point(px, py)

#     def __str__(self): # specify a str conversion
#         return '['+str(self.x)+','+str(self.y)+']'

#     def __repr__(self):
#         return f'Point({self.x},{self.y})'

#     def __eq__(self, p):
#         return self.x == p.x and self.y == p.y
    
#     def __neq__(self, p):
#         return self.x != p.x or self.y != p.y

#     def __getitem__(self, index):
#         if index == 0:
#             return self.x
#         elif index == 1:
#             return self.y
#         return None

#     def __len__(self):
#         return 2
    
# p3 = Point()
# p1 = Point(5,2)
# p2 = Point(8,4)

# print(p1.x, p1.y)
# print(Point.name, p1.name)
# p1.change_name("new name goes here")
# print(Point.name, p1.name)
# Point.name = "new name goes here"
# print(Point.name, p1.name)




### Static methods and dictionaries of functions (use modules instead) ##

# my_dict = {
#     'go': lambda: print("go"),
#     'stay': lambda: print("stay")
# }

# my_dict['go']()
# my_dict['stay']()

# class MyDict():
#     def __init__(self):
#         pass
    
#     @staticmethod
#     def go(x):
#         print("go", x)

#     @staticmethod
#     def stay(x):
#         print("stay", x)

# MyDict.go("home")
# MyDict.stay("here")

# instance = MyDict()
# instance.go("home")




### Inheritance ###

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     class_cool = "yes"

# class AnimalFood(Animal):
#     def __init__(self, name, food):
#         super().__init__(name)
#         self.fav_food = food

# class Squirrel(AnimalFood):
#     def __init__(self, name, food):
#         self.type = "squirrel"
#         super().__init__(name, food) # invoke the parent's initializer

# class Anteater(AnimalFood):
#     def __init__(self, name, food):
#         self.type = "anteater"
#         super().__init__(name, food) # invoke the parent's initializer

# s = Squirrel('Jimmy', 'beans')
# a = Anteater('Earl', 'ants')

# print(s.name, s.type)
# print(a.type, a.fav_food)




### Multiple inheritance with super() ###

# class ParentA:
#     def __init__(self):
#         super().__init__()
#         print('parent a initializer')

# class ParentB:
#     def __init__(self):
#         super().__init__()
#         print('parent b initializer')

# class Child(ParentA, ParentB):
#     def __init__(self):
#         super().__init__()

# c = Child()




### Multiple inheritance without super() ###

# class ParentA:
#     def __init__(self):
#         print('parent a initializer')

# class ParentB:
#     def __init__(self):
#         print('parent b initializer')

# class Child(ParentA, ParentB):
#     def __init__(self):
#         ParentA.__init__(self)
#         ParentB.__init__(self)

# c = Child()




### Composition (you'll need the Point example too) ###

# class Merritt:
#     def __init__(self, x, y):
#         self.name = "Merritt"
#         self.point = Point(x, y)
#         self.my_stuff = []

#     def get_my_point(self):
#         return self.point.x, self.point.y

#     def scale_my_point(self, v):
#         self.point.scale(v)

#     def add_stuff(self, stuff):
#         self.my_stuff.append(stuff)

# me = Merritt(5,6)
# me.scale_my_point(2)
# print(me.get_my_point())
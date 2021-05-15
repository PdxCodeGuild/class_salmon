

x = 0
x = int()
x = int('5')

y = ''
y = str()
y = str(5)

r = range(10)
# for i in range(10)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(5, 2)
print(point.x)



import requests
response = requests.get('https://www.google.com/')
# print(response.text)

with open('text.txt', 'w') as file:
    print(file)
    print(type(file))





class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self):
        print('calling a point')

p = Point(5, 2)
print(p.x)
p()




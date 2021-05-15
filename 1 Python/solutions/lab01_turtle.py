

import turtle


turtle.speed('fastest')

i = 0
n_sides = 50
while i < n_sides:
    turtle.forward(2)
    turtle.left(360/n_sides)
    i += 1

arm_length = 40
body_length = 80
leg_length = 40

turtle.right(90)
turtle.forward(body_length//2)
turtle.left(135)
turtle.forward(arm_length)
turtle.back(arm_length)
turtle.left(90)
turtle.forward(arm_length)
turtle.back(arm_length)
turtle.left(135)
turtle.forward(body_length//2)
turtle.left(45)
turtle.forward(leg_length)
turtle.back(arm_length)
turtle.right(90)
turtle.forward(leg_length)

turtle.done()
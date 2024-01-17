
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
print(rgb_colors)

import turtle as t_m
import random

t = t_m.Turtle()
t_m.colormode(255)
t.speed("fastest")
t.hideturtle()

t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
# t.pendown()
for i in range(10):
    for i in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.penup()
        t.forward(50)
        # t.pendown()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)



screen = t_m.Screen()
screen.exitonclick()
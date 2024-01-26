# from turtle import Turtle, Screen
#
# tt = Turtle()
# tt.shape("turtle")
# tt.color("green")
#
# # simple square
# for i in range(4):
#     tt.forward(100)
#     tt.left(90)
# types of import ways
# import turtle
# ttt = turtle.Turtle()
import random
# from turtle import Turtle
# is better to use we reduce using .Turtle

# from turtle import *
# we import all the methods all that and we can use but we need to be with clarity before doing this

# import turtle as t  #nameing modules as shortform
# tim = t.Turtle()
#  import heros #here it is not there in system so we need to install from pypi using pip

# import heroes
# print((heroes.gen()))

# from turtle import Turtle, Screen
from random import *

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
#
# t.screen.mainloop()
# t.clear()


from turtle import Turtle, Screen
import random
import turtle as tt

t = tt.Turtle()

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("white")

# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps)
#         t.right(30)
#         t.left(20)


# i = 4
# c = ["red", "blue", "green"]
# while True:
#     angle = 360 / i
#     t.color(random.choice(c))
#     for j in range(i):
#         t.forward(100)
#         t.right(angle)
#     i = i + 1

tt.colormode(255)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

t.speed("fastest")
# d = [0, 90, 180, 270]
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(200):
#     t.color(random_color())
#     t.pensize(random.randint(1,5))
#     t.forward(30)
#     t.setheading(random.choice(d))

def drawcircles(size):
    # spirograph
    for k in range(int(360/size)):
        t.color(random_color())
        t.circle(100)
        t.fillcolor(random_color())
        t.setheading(t.heading()+size)

drawcircles(5)










S = Screen()
S.exitonclick()

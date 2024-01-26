from turtle import Turtle, Screen
import random

# t0= Turtle(shape="turtle")
# t0.penup()
# t1 = Turtle(shape="turtle")
# t1.penup()
# t2 = Turtle(shape="turtle")
# t2.penup()
# t3 = Turtle(shape="turtle")
# t3.penup()
# t4 = Turtle(shape="turtle")
# t4.penup()
# t5 = Turtle(shape="turtle")
# t5.penup()
# for i in range(5):
#     t0.color(colors[i])
# t0.goto(x=230, y=30)

s = Screen()
is_on = False

s.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_guess = s.textinput(title="make your bet!!", prompt="which coloured turtle will win!? Enter a color:")
# print(user_guess)
y_pos = [-80,-50,-20,10,40,70]
my_turtles = []

for i in  range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-240, y=y_pos[i])
    my_turtles.append(tim)


if user_guess:
    is_on = True

while is_on:
    for tut in my_turtles:
        if tut.xcor()>230:
            winning_color = tut.pencolor()
            if winning_color == user_guess:
                print("hurry!! you guessed it right your color turtle is won!")
            else:
                print(f"oh!no its incorrect guess {tut.pencolor()} turtle is won")
            is_on = False
            break
        tut.forward(random.randint(0,10))































s.exitonclick()
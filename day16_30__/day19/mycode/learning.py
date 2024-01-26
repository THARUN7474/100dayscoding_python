from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(30)


def move_backward():
    t.backward(30)


def turn_ACW():
    t.left(10)
    # t.setheading(t.heading()+10)


def turn_CW():
    t.setheading(t.heading() - 10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="q", fun=move_backward)
s.onkey(key="s", fun=turn_ACW)
s.onkey(key="a", fun=turn_CW)
s.onkey(key="c", fun=clear)

tt = Turtle()
tt.shape("turtle")
tt.color("green")
tr = Turtle()
tr.shape("turtle")
tr.color("red")
tb = Turtle()
tb.shape("turtle")
tb.color("blue")

t.forward(10)
tt.forward(40)
tr.forward(80)
tb.forward(120)

s.exitonclick()

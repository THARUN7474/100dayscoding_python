from turtle import Turtle

POSTION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]#most used things making them as main variables

    def create_snake(self):
        for pos in POSTION:
            self.add_segment(pos)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)




    def move(self):
        for seg_no in range(len(self.segments)-1, 0, -1):
            self.segments[seg_no].goto(self.segments[seg_no - 1].xcor(), self.segments[seg_no - 1].ycor())
            # here going to the place of prev or front segment like 2 to 1 , 1 to 0 position to enable turining option
        self.head.forward(MOVE_DIST)
        # self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def extend(self):
        self.add_segment(self.segments[-1].position())

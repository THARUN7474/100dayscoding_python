from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=-220,y=260)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.write_score()




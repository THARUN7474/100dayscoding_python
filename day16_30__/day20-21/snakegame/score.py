from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.rand_write()
        self.hideturtle()

    def rand_write(self):
        self.write(f" Score:{self.score}", align="center", font=("Arial", 22, "normal"))

    def increase_score(self):
        self.score = self.score+1
        self.clear()
        self.rand_write()

    def game_over(self):
        self.goto(0,0)
        self.write(f" GAME OVER\nYOUR FINAL SCORE:{self.score}", align="center", font=("Arial", 22, "normal"))

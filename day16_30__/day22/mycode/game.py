from turtle import Screen
from player import Player
from ball import Ball
from score import Score
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pingPong game" "center")
screen.tracer(0)
# screen.update()
r_player = Player((350, 0))
l_player = Player((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_player.go_up, "Up")
screen.onkey(r_player.go_down, "Down")
screen.onkey(l_player.go_up, "a")
screen.onkey(l_player.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_player) < 50 and ball.xcor() > 320)or (ball.distance(l_player) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    if score.r_score > 10 or score.l_score > 10:
        if score.l_score > 10:
            score.game_over("left_player")
        else:
            score.game_over("right_player")
        game_is_on = False






screen.exitonclick()
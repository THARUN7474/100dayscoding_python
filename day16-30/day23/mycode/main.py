import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()


screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() == 290:
        score.increase_score()
        player.repeat()
        cars.level_up()


screen.exitonclick()
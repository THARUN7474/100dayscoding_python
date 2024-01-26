from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVE_INCREMENT

    def create_car(self):
        c = random.randint(1,6)
        if c == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-240, 240))
            new_car.forward(MOVE_INCREMENT)
            self.all_cars.append(new_car)
        self.move_car()

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed = self.move_speed + MOVE_INCREMENT


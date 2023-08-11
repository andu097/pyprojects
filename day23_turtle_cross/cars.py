from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# crearea masinilor

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_c = Turtle()
            new_c.shape('square')
            new_c.color(random.choice(COLORS))
            new_c.setheading(180)
            new_c.penup()
            new_c.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_c.goto(280, random_y)
            self.all_cars.append(new_c)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

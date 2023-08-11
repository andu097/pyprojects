from time import sleep
from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard

# setarea ecranului
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

# initierea obiectelor
p = Player()
c = Car()
score = Scoreboard()

# loop infinit pentru a juca jocul
game_on = True

while game_on:
    sleep(0.1)
    s.update()

    s.listen()
    s.onkey(p.move, "Up")

    c.create_car()
    c.move_car()
    if p.is_at_finish():
        p.reset_position()
        c.speed_up()
        score.increase_score()
    for car in c.all_cars:
        if car.distance(p) < 20:
            score.game_over()
            game_on = False

s.exitonclick()

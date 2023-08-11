from turtle import Screen
from snake import Snake
from EGG import Food
from scoreboard import Scoreboard
import time

# setup pentru fereastra jocului
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# initierea obiectelor
snake = Snake()
food = Food()
score = Scoreboard()

# setarea comenzilor
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# loop infinit pentru a face jocul sa ruleze la infinit
game_on = True

while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 20:
        snake.extend()
        score.increase_score()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        score.reset_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            score.reset_score()


screen.exitonclick()

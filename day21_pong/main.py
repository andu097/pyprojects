from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


# setarea ecranului
s = Screen()

s.setup(width=800, height=600)
s.title('Pong')
s.bgcolor('black')
s.tracer(0)

# setarea paletelor pentru pong
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((325, 270))
l_scoreboard = Scoreboard((-325, 270))

# setarea comenzilor de control
s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")


# loop infinit pentru a jucat jocul
game_on = True

while game_on:
    s.update()
    sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset()
        l_scoreboard.increase_score()
    elif ball.xcor() < -380:
        ball.reset()
        r_scoreboard.increase_score()

s.exitonclick()

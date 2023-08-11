from turtle import Turtle, Screen


t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_right():
    t.right(10)


def move_left():
    t.left(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

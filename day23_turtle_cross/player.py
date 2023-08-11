from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280

# crearea testoasei jucatorului

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('Blue')
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
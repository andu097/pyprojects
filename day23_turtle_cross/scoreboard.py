from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# crearea tabelei de marcaj

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, 270)
        self.color('black')
        self.hideturtle()
        self.write(f"Level: {self.level} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", move=False, align='center', font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

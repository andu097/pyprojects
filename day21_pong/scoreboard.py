from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

# crearea tabelei de marcaj

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", move=False, align='center', font=('Arial', 20, 'normal'))
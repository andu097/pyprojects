from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_number in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_number])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_number])
    all_turtle.append(turtle)


if bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won the winner is {winning_color}")
            else:
                print(f"You lose! The winner is {winning_color}")
            race_on = False



screen.exitonclick()

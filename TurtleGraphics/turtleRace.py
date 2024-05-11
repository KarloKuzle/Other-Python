from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Whitch turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle])
    t.pu()
    t.goto(-230, y_pos[turtle])
    all_turtles.append(t)


if user_bet:
    is_race_on = True


while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        t.forward(random.randint(0, 10))

screen.exitonclick()
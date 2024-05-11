import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple



t = Turtle()

t.speed("fastest")

t.pensize(2)

for i in range(0, 360, 5):
    t.color(random_color())
    t.circle(100)
    t.lt(5)

screen = Screen()
screen.exitonclick()
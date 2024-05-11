from turtle import Turtle, Screen

t = Turtle()

t.down()
for i in range(4):
    t.forward(100)
    t.lt(90)
t.up()

screen = Screen()
screen.exitonclick()


from turtle import Turtle, Screen

t = Turtle()

for i in range(4, 10, 1):
    for j in range(i):
        t.fd(100)
        t.lt(360 / i)

screen = Screen()
screen.exitonclick()


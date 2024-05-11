from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(30)

def move_backwards():
    t.backward(30)

def turn_left():
    t.lt(10)

def turn_right():
    t.rt(10)

def clear_drawing():
    t.pu()
    t.clear()
    t.goto(0, 0)
    t.pd()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.listen()
screen.exitonclick()
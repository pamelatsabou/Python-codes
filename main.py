# Turtle: listening keys from keyboard

from turtle import Turtle, Screen

pam = Turtle()
screen = Screen()
pam.speed("fastest")

'''
def move_forward():
    pam.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
'''


def move_forwards():
    pam.forward(50)


def move_backwards():
    pam.back(50)


def move_counter_clockwise():
    new_heading = pam.heading() + 10
    pam.setheading(new_heading)


def draw_circle():
    pam.circle(50, 45, 5)


def move_clockwise():
    new_heading = pam.heading() - 10
    pam.setheading(new_heading)


def clear_drawing():
    pam.clear()
    pam.reset()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_counter_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear_drawing)
screen.onkey(key="Q", fun=draw_circle)


screen.exitonclick()

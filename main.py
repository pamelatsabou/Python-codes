# Turtle module

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

turtle.colormode(255)

timmy.shape("turtle")
timmy.color("blue")

##################################################
'''
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
'''
###################################################

'''
for _ in range(20):
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    timmy.forward(5)
'''
###################################################
'''
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(5):
        timmy.forward(100)
        timmy.right(angle)

for side_n in range(3,11):
    draw_shape(side_n)
'''

#################################################


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# generating random colors and walks
'''
timmy.hideturtle()
pen_size = 1
timmy.pensize(pen_size)
var = random.randint(1, 100)

for _ in range(200):
    moves = ["timmy.forward(var)", "timmy.left(var)", "timmy.right(var)"]
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    timmy.color(random_color())
    random_walk = random.choice(moves)
    timmy.pensize(pen_size)
    timmy.speed("fastest")
    if random_walk == "timmy.forward(var)":
        timmy.forward(random.randint(10, 50))
    elif random_walk == "timmy.left(var)":
        timmy.left(90)
    elif random_walk == "timmy.right(var)":
        timmy.right(90)
    pen_size += 0.1
'''

###################################################


def draw_spirograph(size_of_graph):
    for _ in range(360 // size_of_graph):
        timmy.color(random_color())
        timmy.circle(150)
        timmy.left(size_of_graph)
        timmy.speed("fastest")


draw_spirograph(3)
# drawing spirograph




screen = Screen()
screen.exitonclick()

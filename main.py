# The Hirst Painting Project Part 1

'''
import colorgram
rgb_colors = []
colors = colorgram.extract('index.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
import turtle
from turtle import Turtle, Screen
import random

color_list = [(202, 164, 189), (230, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (10, 86, 90), (81, 140, 129), (140, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
pam = Turtle()
turtle.colormode(255)
pam.speed("fastest")

pam.setheading(225)
pam.forward(255)
pam.setheading(0)
pam.hideturtle()

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    pam.dot(20, random.choice(color_list))
    pam.penup()
    pam.forward(50)
    if dot_count % 10 == 0:
        pam.setheading(90)
        pam.forward(50)
        pam.setheading(180)
        pam.forward(500)
        pam.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
# Arcade game

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong Game")
screen.tracer(0)

pam = Turtle()
pam.speed("fastest")
pam.color("white")
pam.hideturtle()
pam.penup()
pam.goto(0, -250)
pam.left(90)

for _ in range(34):
    pam.pensize(3)
    pam.pendown()
    pam.forward(5)
    pam.penup()
    pam.forward(10)

l_paddle = Paddle((-320, 0))
r_paddle = Paddle((320, 0))
score = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with the wall
    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce_vertically()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > 300) or (ball.distance(l_paddle) <= 50 and ball.xcor() < -300):
        ball.bounce_horizontally()

    # Detect r_paddle misses
    if ball.xcor() > 330:
        ball.reset_position()
        score.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -330:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

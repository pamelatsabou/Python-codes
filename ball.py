from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.speed("fastest")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertically(self):
        self.y_move *= -1

    def bounce_horizontally(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_horizontally()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

pam = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(pam.move_forwards, "Up")
# screen.onkey(pam.move_backwards, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_movements()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(pam) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if pam.is_at_finish_line():
        pam.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

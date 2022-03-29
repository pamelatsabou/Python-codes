# Hurdles loop challenge
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(1, 7):
    move()
    jump()
'''
# Hurdle3 while loop with if statement

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front() == True:
        jump()
    else:
        move()


# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    else:
        turn_left()

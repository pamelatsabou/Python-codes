# Treasure island

print("""
Welcome to Treasure Island.
Your mission is to find the treasure.""")
choice1 = input("You're at the cross-road. Where do you want to go? 'left' or 'right'?\n").lower()
if choice1 == "right":
    print("Game over")
else:
    choice2 = input("""
    You come to a lake. 
    There's an island in the middle of the lake. 
    Type 'wait' to wait for a boat.
    Type 'swim' to swim across.\n""").lower()
    if choice2 == 'swim':
        print("Game over")
    else:
        choice3 = input("""
        You arrive at the island unharmed.
        There's a house with 3 doors, the red, the yellow and the blue.
        Which one do you choose?\n""").lower()
        if choice3 == 'yellow' or choice3 == 'red':
            print("You entered the wrong room. Game over.")
        else:
            print("You win")


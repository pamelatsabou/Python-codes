# Rock-Paper-Scissors

import random

choice_list = ["rock", "paper", "scissors"]

user_number = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))
user_choice = choice_list[user_number]
print(f"You chose: {user_choice}")
computer_choice = random.choice(choice_list)
print(f"Computer chose: {computer_choice}")

if user_number == 0:
    if computer_choice == 'paper':
        print("You lose")
    elif computer_choice == 'scissors':
        print("You win")
    elif computer_choice == 'rock':
        print("Draw")
elif user_number == 1:
    if computer_choice == 'scissors':
        print("You lose")
    elif computer_choice == 'rock':
        print("You win")
    elif computer_choice == 'paper':
        print("Draw")
elif user_number == 2:
    if computer_choice == 'rock':
        print("You lose")
    elif computer_choice == 'paper':
        print("You win")
    elif computer_choice == 'scissors':
        print("Draw")


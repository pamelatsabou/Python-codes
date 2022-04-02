# Number Guessing Game

import random

play_again = True

while play_again:
    number = random.choice(range(1, 101))
    is_over = False
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5

    def compare(user_guess, true_number):
        global lives
        global is_over
        if user_guess == true_number:
            is_over = True
            return "You guessed the number, you win"
        elif lives == 0:
            is_over = True
            return "You ran out of guesses, you lose"

        elif user_guess < true_number:
            return "Too low.\nGuess again."
        elif user_guess > true_number:
            return "Too high.\nGuess again."

    while not is_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        lives -= 1
        guess = int(input("Make a guess: "))
        print(compare(guess, number))
        if lives == 0:
            is_over = True

    answer = input("Would you like to play another game? Type 'y' or 'n': ")
    if answer == 'n':
        play_again = False


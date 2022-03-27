# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input(f"How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level; where the letters are seperated from the numbers and symbols
'''letters_chosen = ''
numbers_chosen = ''
symbols_chosen = ''

for _ in range(0, num_letters):
    chosen_letter = random.choice(letters)
    letters_chosen += chosen_letter

for _ in range(0, num_numbers):
    chosen_number = random.choice(numbers)
    numbers_chosen += chosen_number

for _ in range(0, num_symbols):
    chosen_symbol = random.choice(symbols)
    symbols_chosen += chosen_symbol

print(f"{letters_chosen}{numbers_chosen}{symbols_chosen}")
'''

# Difficult level; where the password has all characters mixed

password = ""
order = ['chosen_letter', 'chosen_number', 'chosen_symbol']
total_length = num_numbers + num_symbols + num_letters
count_letters = 0
count_numbers = 0
count_symbols = 0

for _ in range(0, total_length):
    chosen_letter = random.choice(letters)
    chosen_number = random.choice(numbers)
    chosen_symbol = random.choice(symbols)
    chosen_character = random.choice(order)
    if chosen_character == 'chosen_letter' and num_letters >= count_letters:
        password += chosen_letter
        count_letters += 1
    elif chosen_character == 'chosen_number' and num_numbers >= count_numbers:
        password += chosen_number
        count_numbers += 1
    elif chosen_character == 'chosen_symbol' and num_symbols >= count_symbols:
        password += chosen_symbol
        count_symbols

print(f"Your password is {password}")







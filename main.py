# Higher Lower

from game_data import data
from art import vs, logo
import random

print(logo)
score = 0
is_game_over = False

account_a = random.choice(data)

while not is_game_over:
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    def random_person(random_account):
        name = random_account["name"]
        description = random_account["description"]
        country = random_account["country"]
        return f"{name}, a {description}, from {country}"


    def compare():
        """returns true if user enters 'a' which in this case should be greater"""
        follower_count_a = account_a["follower_count"]
        follower_count_b = account_b["follower_count"]
        print(follower_count_a)  # , to check the number of followers for 'a'
        print(follower_count_b)  # , to check for 'b'
        if follower_count_a > follower_count_b:
            return guess == "A"
        elif follower_count_b > follower_count_a:
            return guess == "B"


    print(f"Compare A: {random_person(account_a)}.")
    print(vs)
    print(f"Against B: {random_person(account_b)}.")
    guess = input("Which has more followers? Type 'A' or 'B': ").lower()

    if not compare():
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b

    elif compare():
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True

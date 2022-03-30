# Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)


# Secret Auction Program

bidders = {}
turns = 1
other_bidder_exists = True


def secret_auction(name_of_bidder, bid_amount):
    highest_bid = 0
    '''Formats the names and bids entered into a dictionary'''
    for _ in range(turns):
        bidders[name_of_bidder] = bid_amount
        if bid_amount > highest_bid:
            highest_bid = bid_amount
#    print(bidders) to check code
    print(f"The winner is {name} with a bid of ${highest_bid}")


while other_bidder_exists:
    name = input("Enter your name: ")
    bid = int(input("What is your bid? $"))
    answer = input("Is there another bidder? ")

    turns += 1

    if answer == 'no':
        other_bidder_exists = False
        secret_auction(name, bid)
# tip calculator

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
tip_as_percent = percentage_tip / 100
pay_per_person = round(((tip_as_percent * total_bill) + total_bill) / num_of_people, 2)
final_amount = "{:.2f}".format(pay_per_person)
print(f"Each person should pay ${final_amount}")
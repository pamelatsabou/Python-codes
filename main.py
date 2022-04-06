# Coffee Machine

from data import MENU, resources

# print report
# check resource sufficient?
# Process coins
# Check transaction successful?
# Make coffee


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        # comparing each value of the resource dictionary with that of the ordered drink
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?$ "))
    dimes = int(input("How many dimes?$ "))
    nickles = int(input("How many nickles?$ "))
    pennies = int(input("How many pennies?$ "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def transaction_successful(amount_received, drink_cost):
    if amount_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif amount_received > drink_cost:
        global profit
        balance = round(amount_received - drink_cost, 2)
        profit += drink_cost
        print(f"Here is ${balance} in change.")
        return True
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


profit = 0
is_on = True

while is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        is_on = False
    elif request == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {profit}")
    else:
        drink = MENU[request]
        # print(drink)
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(request, drink["ingredients"])

# Coffee machine using oop

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
# check resource sufficient?
# Process coins
# Check transaction successful?
# Make coffee

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        is_on = False
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)








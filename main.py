"""This is an OOP coffee maker application."""
# Imports
import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

print(logo)

# Instantiate the class
make_coffee = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()


def clear():
    """This function clears the console."""
    os.system('clear')


# The application
turn_off = False
while not turn_off:
    default = input('Do you want to make a coffee? ').lower()

    clear()
    print(logo)

    if default == 'yes':
        print('\nThis coffee maker only makes Espresso, Latte and Cappuccino.')
        user_drink = input('What kind of coffee do you want? ').lower()
        available = menu.find_drink(user_drink)
        if available:
            if make_coffee.is_resource_sufficient(available):
                print(f'The price for {available.name} price is €{available.cost:.2f}')
                if payment.make_payment(available.cost):
                    make_coffee.make_coffee(available)
    elif default == 'no':
        turn_off = True
        print('Okay.')
    elif default == 'off':
        turn_off = True
        print('The Coffee Maker is off.')
    elif default == 'report':
        print('Coffee Maker Report:')
        make_coffee.report()
        payment.report()
    else:
        print('Invalid response.\n')




# from turtle import *
#
# mickey = Turtle()
# mickey.shape("turtle")
# mickey.color("coral")
# mickey.width(4)
#
# mickey.fd(200)
# mickey.left(120)
# mickey.fd(200)
# mickey.left(120)
# mickey.fd(200)
#
# my_screen = Screen()
# my_screen.exitonclick()

#######################################################################################################


from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_running = True
while machine_running:
	options = menu.get_items()
	selection = input(f"What would you like? ({options}): ").lower()
	if selection == "off":
		machine_running = False
	elif selection == "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(selection)
		if drink is not None:
			if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)

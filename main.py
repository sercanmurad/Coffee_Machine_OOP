from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu=Menu()
is_on=True

#2.Check resources sufficient

while is_on:
    options=menu.get_items()
    choice=input(f"What whould you like to drink: ({options})")
    if choice=="off":
        is_on=False
    elif  choice == "report":
        # 1.Print report
        my_money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            #3Process coins
            #4Check transaction
            if my_money_machine.make_payment(drink.cost):
                #5 Make coffee
                coffee_maker.make_coffee(drink)





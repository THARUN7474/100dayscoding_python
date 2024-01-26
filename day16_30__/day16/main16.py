from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
M = Menu()
# MI = MenuItem()
m_machine.report()
is_on = True

while is_on :
    user_req = input(f"What would you like?{M.get_items()}")
    if user_req == "off":
        is_on = False
    elif user_req == "report":
        coffe_maker.report()
        m_machine.report()
    else:
        item = M.find_drink(user_req)
        if item == "OFF":
            is_on = False
        elif coffe_maker.is_resource_sufficient(item):
            if m_machine.make_payment(item.cost):
                coffe_maker.make_coffee(item)

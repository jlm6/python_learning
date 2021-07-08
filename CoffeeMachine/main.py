from menu import MENU, resources
from coin import coins
from ffff import check_material
from total_coin import totalcoin


# TODO Ask client what they need
money = 0
is_over = False
while not is_over:
    client = input("What would you like? (espresso/latte/cappuccino): ")
    if client == "report":
        for item in resources:
            if item == "coffee":
                print(f"{item} : {resources[item]}g")
            else:
                print(f"{item} : {resources[item]}ml")
        print(f"money: ${money}")
        client = input("What would you like? (espresso/latte/cappuccino): ")

    if client == "off":
        is_over = True
        break

# TODO to check if have enough ingradients espresso, latte and cappucino
    if check_material(client, MENU):
        total = totalcoin()
    else:
        break

    if MENU[client]['cost'] > total:
        print("Sorry that's not enough money. Money refunded.")
    elif MENU[client]['cost'] <= total:
        water_remain = resources['water'] - MENU[client]['ingredients']['water']
        coffee_remain = resources['coffee'] - MENU[client]['ingredients']['coffee']
        if 'milk' in MENU[client]['ingredients']:
            milk_remain = resources['milk'] - MENU[client]['ingredients']['milk']
        else:
            milk_remain = resources['milk']

        resources['water'] = water_remain
        resources['milk'] = milk_remain
        resources['coffee'] = coffee_remain
        money_exchange = total - MENU[client]['cost']
        for item in resources:
            if item == "coffee":
                print(f"{item} : {resources[item]}g")
            else:
                print(f"{item} : {resources[item]}ml")
        print(f"Money: ${MENU[client]['cost']}")
        print(f"Here is ${money_exchange} dollars in change.")
        print("Here is your latte. Enjoy!")














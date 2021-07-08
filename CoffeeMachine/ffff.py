from menu import MENU, resources
from coin import coins

def check_material(client, MENU):
    noway = 1
    if client not in MENU:
        print(f"We cant offer you {client}, NOT Found")
        noway = 0

    for item in MENU:
        if client == item:
            if item == 'espresso':
                if resources['water'] < MENU[item]['ingredients']['water']:
                    print("Sorry there is not enough water.")
                    noway = 0


                if resources['coffee'] < MENU[item]['ingredients']['coffee']:
                    print("Sorry there is not enough coffee.")
                    noway = 0


            else:
                if resources['water'] < MENU[item]['ingredients']['water']:
                    print("Sorry there is not enough water.")
                    check = 0


                if resources['coffee'] < MENU[item]['ingredients']['coffee']:
                    print("Sorry there is not enough coffee.")
                    noway = 0


                if resources['milk'] < MENU['latte']['ingredients']['milk']:
                    print("Sorry there is not enough milk.")
                    noway = 0

    return noway

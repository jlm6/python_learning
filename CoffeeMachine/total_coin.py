from coin import coins

def totalcoin():
    print("Please insert coins.")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickles = int(input("how many nickles?: "))
    num_pennies = int(input("how many pennies?: "))
    total = float(coins['quarters']) * num_quarters + float(coins['dimes']) * num_dimes + float(coins['nickles']) * num_nickles + float(coins['pennies']) * num_pennies
    return total

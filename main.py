from menu import MENU, resources
from art import logo

print(logo)


def print_report(total):
    """Prints the current resources and money in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total:.2f}")


def make_coffee(drink_name):
    """Deducts resources to make a drink and checks resource availability.

    Args:
        drink_name (str): Name of the drink to make.

    Returns:
        bool: True if drink was made, False otherwise.
    """
    for key, value in MENU[drink_name]["ingredients"].items():
        resources[key] -= value
        if resources[key] < 0:
            print(f"Sorry there is not enough {key}.")
            resources[key] += value
            return False
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    return True


def coins_operate():
    """Prompts user for coins and calculates total inserted value.

    Returns:
        float: Total value of inserted coins.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total, 2)


def process_drink_choice(drink_choice):
    """Processes user's drink choice, handles payment, and makes the drink.

    Args:
        drink_choice (str): User's chosen drink identifier.
    """
    money = coins_operate()
    if money >= MENU[drink_choice]["cost"]:
        money -= MENU[drink_choice]["cost"]
        if make_coffee(drink_choice):
            print(f"Here is ${money:.2f} in change.")
        else:
            print("Sorry, we couldn't make your drink.")
    else:
        print("Sorry that's not enough money. Money refunded.")


DRINK_IDENTIFIERS = {
    'esp': 'espresso',
    'lat': 'latte',
    'cap': 'cappuccino'
}

machine_total = 0
coffee_loop = True

while coffee_loop:
    if any(resource < 0 for resource in resources.values()):
        print("Sorry, there is not enough resources to make another drink.")
        coffee_loop = False
        break

    user_input = input("What would you like? (espresso = 'esp' | latte = 'lat' | cappuccino = 'cap' | report | off) ")

    if user_input in DRINK_IDENTIFIERS:
        process_drink_choice(DRINK_IDENTIFIERS[user_input])
        machine_total += MENU[DRINK_IDENTIFIERS[user_input]]["cost"]
    elif user_input == 'report':
        print_report(machine_total)
    elif user_input == 'off':
        print("Turning off the coffee machine.")
        coffee_loop = False
    else:
        print("Invalid input")

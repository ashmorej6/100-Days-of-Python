MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(water, milk, coffee):
    if resources["water"] < water:
        print("Sorry there is not enough water.")
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
    else:
        return True

def collect_payment():
    print(f"Please insert £{MENU[user_choice]["cost"]}0")
    pounds = float(input("How many £ coins?: "))
    fifties = float(input("How many 50p coins?: "))
    twenties = float(input("How many 20p coins?: "))
    tens = float(input("How many 10p coins?: "))
    payment_in = []
    payment_in.append(pounds * 1.0)
    payment_in.append(fifties * 0.5)
    payment_in.append(twenties * 0.2)
    payment_in.append(tens * 0.1)
    return sum(payment_in)

def check_transaction(payment, cost):
    if payment < cost:
        confirm = False
        return confirm
    else:
        confirm = True
        return confirm

def is_change(payment, cost):
    if payment > cost:
        change = payment - cost
        return change

power_on = True
while power_on:
    #payment = 0
    #change = 0
    ###Collects user input and carries out functions like "OFF" and "Report"
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        power_on = False
    elif user_choice == "report":
        for key, value in resources.items():
            print(f"{key} : {value}")
    else:
        ###Checks what's needed for users drink of choice and saves to variables for resource check
        water_use = MENU[user_choice]["ingredients"]["water"]
        milk_use = MENU[user_choice]["ingredients"]["milk"]
        coffee_use = MENU[user_choice]["ingredients"]["coffee"]
        cost = MENU[user_choice]["cost"]
        ###Check if enough resources and then collect payment - store money inputted in payment variable
        if check_resources(water_use, milk_use, coffee_use):
            payment = collect_payment()
            confirm_transaction = check_transaction(payment, cost)
            change = is_change(payment, cost)

            if confirm_transaction:
                resources["water"] -= water_use
                resources["milk"] -= milk_use
                resources["coffee"] -= coffee_use
                resources["money"] += cost
                print(f"Here is your {user_choice} ☕️")
                if change > 0:
                    print(f"Here is your change of £{change}0")
            elif not confirm_transaction:
                print("Sorry that's not enough money. Money refunded.")

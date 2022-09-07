MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def select_option(menu, resources):
    choice = input("What would you like? (espresso/latte/cappuccino) ")

    if choice == 'report':
        for y in resources:
            if y == "water" or y == "milk":
                print(f"{resources[y]}ml")
            elif y == "coffee":
                print(f"{resources[y]}g")
            else:
                print(f"£{resources[y]}")
    elif choice == 'off':
        return choice
    elif choice == 'espresso':
        return menu["espresso"]
    elif choice == 'cappuccino':
        return menu["cappuccino"]
    elif choice == 'latte':
        return menu["latte"]


def check_resources(ingredients, resources):
    for ingredient in ingredients:
      if ingredients[ingredient] > resources[ingredient]:
        print(f"Sorry, there isn't enough {ingredient}.")
        return False
    return True


def get_money(choice, resources):
    price = "{:.2f}".format(choice['cost'])
    print(f"The price is: £{price}")
    print("Please insert coins.")
    tens = int(input("How many tens?: ")) * 0.1
    twenties = int(input("How many twenties?: ")) * 0.2
    fifties = int(input("How many fifties?: ")) * 0.5
    pounds = int(input("How many pounds?: "))
    sum = (tens + twenties + fifties + pounds)
    if sum < choice['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif sum > choice['cost']:
        resources['money'] += choice['cost']
        print(f"Your change is £{'{:.2f}'.format(sum - float(price))}")


def make_drink(ingredients, resources):
  for ingredient in ingredients:
    resources[ingredient] -= ingredients[ingredient]
  print("Here is your drink! Enjoy")

machine_on = True
while machine_on:
    choice = select_option(MENU, resources)
    if choice == None:
        continue
    elif choice == 'off':
        machine_on = False
        continue
    if not check_resources(choice['ingredients'], resources):
        continue

    get_money(choice, resources)
    make_drink(choice['ingredients'], resources)

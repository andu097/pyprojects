from coffee_menu import MENU, resources

main_menu = MENU
res = resources
water_available = res["water"]
milk_available = res['milk']
coffee_available = res['coffee']
machine = "on"
credit = 0


def get_coffee(dict1):
    global water_available
    global milk_available
    global coffee_available
    global credit
    if order == "espresso":
        dict1[order]['ingredients']['milk'] = 0
    water_needed = dict1[order]['ingredients']['water']
    milk_needed = dict1[order]['ingredients']['milk']
    coffee_needed = dict1[order]['ingredients']['coffee']
    coffee_cost = dict1[order]['cost']
    if water_available > water_needed and milk_available > milk_needed and coffee_available > coffee_needed:
        print("All resources needed are available!")
        print(f"Credit needed: {coffee_cost}$")
        credit = float(input("Insert credits: $"))
        if credit > coffee_cost:
            water_available -= water_needed
            milk_available -= milk_needed
            coffee_available -= coffee_needed
            credit -= coffee_cost
            get_resources()
        else:
            print("Not enough credit!")
    else:
        print("Not enough resources!")


def get_resources():
    print(f"Resources in machine:\nWater: {water_available}\nCoffee: {coffee_available}\nMilk: {milk_available}")


while machine == "on":
    order = input("Can i get your order?: ").lower()
    if order == "report":
        get_resources()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        get_coffee(main_menu)
    elif order == "off":
        machine = "off"
    else:
        print("Command not available!")

import tkinter as tk

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(item):
    for ingredient in MENU[item]["ingredients"]:
        resources[ingredient] -= MENU[item]["ingredients"][ingredient]
    print(f"Here is your {item}")


def restock(a):
    for item in a:
        a[item] = stock[item]
    print("Resources refilled!!")
    print("\n")


def process_money():
    payment = int(money_input.get())
    if payment < drink["cost"]:
        result_text.set("Insufficient funds, payment refunded")
    else:
        change = payment - drink["cost"]
        result_text.set(f"Here is your {choice} ☕️. Enjoy! Your change is {change}$")
        global profit
        profit += drink["cost"]
        is_resource_sufficient(drink["ingredients"])
        make_coffee(choice)


def order_drink():
    global choice, drink
    choice = drink_input.get().lower()
    if choice == "off":
        window.destroy()
    elif choice == "report":
        result_text.set(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nProfit: {profit}$")
    elif choice == "restock":
        restock(resources)
        result_text.set("Resources refilled!")
    elif choice not in MENU:
        result_text.set("Invalid choice!")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            result_text.set(f"Price: {drink['cost']}$")
        else:
            result_text.set(f"Sorry, there is not enough resources to make {choice} ☕️.")



window = tk.Tk()
window.title("Coffee Machine")

drink_label = tk.Label(window, text="What would you like to drink?", font=("Arial", 12))
drink_label.pack(pady=10)

drink_choice_label = tk.Label(window, text="espresso, latte, cappuccino", font=("Arial", 12))
drink_choice_label.pack(pady=10)

drink_input = tk.Entry(window, font=("Arial", 12))
drink_input.pack()

order_button = tk.Button(window, text="Order", font=("Arial", 12), command=order_drink)
order_button.pack(pady=10)

money_label = tk.Label(window, text="Insert money (USD):", font=("Arial", 12))
money_label.pack()

money_input = tk.Entry(window, font=("Arial", 12))
money_input.pack()

process_button = tk.Button(window, text="Process", font=("Arial", 12), command=process_money)
process_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()

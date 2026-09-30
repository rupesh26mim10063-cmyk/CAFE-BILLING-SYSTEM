# orders.py
# Module 2: Order taking (customer picks items and quantity)

import menu
from validation import get_number


def add_to_order(order, item_name, price, quantity):
    # each order entry is (name, quantity, price, amount)
    amount = price * quantity
    order.append((item_name, quantity, price, amount))
    return amount


def take_order():
    order = []

    while True:
        menu.show_menu()
        print("0. Finish order")

        choice = get_number("\nEnter item number: ", 0, 999)

        if choice == 0:
            break

        item = menu.get_item(choice)
        if item is None:
            print("Invalid choice!")
            continue

        quantity = get_number("Enter quantity (1-50): ", 1, 50)
        add_to_order(order, item[0], item[1], quantity)
        print(item[0], "added to your order.")

    return order

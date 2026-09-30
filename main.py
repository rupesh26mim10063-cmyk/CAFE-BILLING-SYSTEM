# main.py
# Cafe Billing System - run this file to start the program

import menu
import billing
import storage
from orders import take_order
from validation import get_number, get_name


def add_menu_item():
    name = input("Enter new item name: ").strip()
    if name == "":
        print("Item name cannot be empty.")
        return
    price = get_number("Enter price (1-5000): ", 1, 5000)
    number = menu.add_item(name, price)
    print(name, "added with number", number)


def remove_menu_item():
    menu.show_menu()
    number = get_number("Enter item number to remove: ", 1, 999)
    if menu.remove_item(number):
        print("Item removed.")
    else:
        print("Item number not found.")


def new_bill():
    customer_name = get_name("Enter customer name: ")
    order = take_order()

    if len(order) == 0:
        print("No items ordered, so no bill was made.")
        return

    total = billing.print_bill(customer_name, order)
    storage.save_bill(customer_name, total)


def show_summary():
    count, total_sales = storage.sales_summary()
    print("\n----- SALES SUMMARY -----")
    print("Total bills  :", count)
    print("Total sales  : ₹", total_sales)


def main():
    print("CAFE BILLING")

    while True:
        print("\n1. View menu")
        print("2. Add item to menu")
        print("3. Remove item from menu")
        print("4. New order / Generate bill")
        print("5. Sales summary")
        print("6. Exit")

        choice = get_number("Enter your choice: ", 1, 6)

        if choice == 1:
            menu.show_menu()
        elif choice == 2:
            add_menu_item()
        elif choice == 3:
            remove_menu_item()
        elif choice == 4:
            new_bill()
        elif choice == 5:
            show_summary()
        else:
            print("Goodbye!")
            break


try:
    main()
except KeyboardInterrupt:
    print("\nProgram stopped by user.")

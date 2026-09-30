# menu.py
# Module 1: Menu management (view, add and remove items)

menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("French Fries", 100),
    4: ("Sandwich", 80),
    5: ("Cold Drink", 50),
    6: ("Tea", 15),
    7: ("Masala Tea", 25),
    8: ("Hot Chocolate", 75),
    9: ("Coffee Latte", 80),
    10: ("Expresso", 50),
    11: ("Macha", 60),
    12: ("Chocolate Pastry", 65),
    13: ("Pineapple Pastry", 45),
    14: ("Butterscotch Pastry", 50),
    15: ("Any Popsickle", 35)
}


def show_menu():
    print("\n MENU")
    for number, item in menu.items():
        print(number, ".", item[0], "- ₹", item[1])


def get_item(number):
    # returns (name, price) or None if the number is not in the menu
    return menu.get(number)


def add_item(name, price):
    # new item gets the next free number
    if len(menu) == 0:
        number = 1
    else:
        number = max(menu) + 1
    menu[number] = (name, price)
    return number


def remove_item(number):
    # returns True if removed, False if the number was not found
    if number in menu:
        del menu[number]
        return True
    return False

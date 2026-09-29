print("CAFE BILLING")

# Get customer name
customer_name = input("Enter customer name: ")

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
    10:("Expresso", 50),
    11:("Macha", 60),
    12:("Chocolate Pastry", 65),
    13:("Pineapple Pastry", 45),
    14:("Butterscotch Pastry", 50),
    15:("Any Popsickle", 35)
}

total = 0
orders = []

while True:
    print("\n MENU")

    for number, item in menu.items():
        print(number, ".", item[0], "- ₹", item[1])

    print("16. Generate Bill")

    choice = int(input("\nEnter item number: "))

    if choice == 16:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        price = menu[choice][1]
        amount = price * quantity

        orders.append((item_name, quantity, price, amount))
        total += amount

        print(item_name, "added to your order.")

    else:
        print("Invalid choice!")

# Generate bill
print("FINAL BILL")

print("Customer Name :", customer_name)

for item in orders:
    print(item[0], "x", item[1], " = ₹", item[3])

print("Subtotal: ₹", total)

gst = total * 0.05
grand_total = total + gst

print("GST (5%)       : ₹", round(gst, 2))
print("TOTAL          : ₹", round(grand_total, 2))
print("Thank You! Visit Again")
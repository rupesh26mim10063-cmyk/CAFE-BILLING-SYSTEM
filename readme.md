
# Cafe Billing System

## Overview

This is a simple command-line program for a cafe. It shows a menu of food and drinks, lets the customer order as many items as they like, and then prints out a final bill — including a 5% GST charge — at the end.

## Features

- **Customer name** — asks for the customer's name at the start, and it will be printed on the bill.
- **Menu display** — shows a numbered list of all the food and drinks on the menu, with prices.
- **Order items** — lets the customer pick an item by number and choose how many they want.
- **Running total** — keeps adding up the cost of everything ordered as you go.
- **Error checking** — if you type a number that isn't on the menu, it tells you it's an invalid choice instead of crashing.
- **Final bill** — once you're done, it prints every item ordered, the subtotal, the GST (5%), and the grand total.

## Technologies used

- **Python** — the whole program is written in Python, using only the standard built-in tools (no extra libraries needed)

## Installing and running steps

1. Make sure Python is installed on your computer.
2. Copy the code into a file, e.g. `cafe_billing.py`.
3. Open a terminal in this folder and run:
```python cafe_billing.py ```
4. When asked, type in your name.
5. To order an item, type the item number and the quantity you want. Continue this process for as many items as you wish.
6. Once you’re done, enter **16** to get the bill.

## How to test it

1. Run the program and enter a customer name.
2. Add several different items to your order, including at least one item with a quantity of more than 1.
3. Try typing a number that is not on the menu (like 99) and you'll see it prints "Invalid choice!" instead of exiting the program.
4. Press 16 to create the bill and check that:
- For each item you ordered, all quantities and amounts are correct
- The subtotal adds up right
- The GST is 5% exactly of the subtotal
   Total = Subtotal + GST Tax
5. Run it again, do not put in any orders, type 16 to see how it handles an empty order.

## Screenshots

<img width="372" height="744" alt="image" src="https://github.com/user-attachments/assets/0e11e251-398b-436e-874c-38c7672a5f6f" />
<img width="372" height="744" alt="image" src="https://github.com/user-attachments/assets/90e7793b-81f3-4aef-8be0-dfbaaa851fad" />


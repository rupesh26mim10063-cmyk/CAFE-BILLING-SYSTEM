
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

Tested:
<img width="1366" height="768" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/f6ecafe6-aa7f-4a91-9810-6c83ada004ae" />


MENU:
<img width="988" height="620" alt="im1" src="https://github.com/user-attachments/assets/56f86e1e-ec78-4846-aee3-88eff58a736d" />

Add & Remove Items:
<img width="990" height="610" alt="im2" src="https://github.com/user-attachments/assets/0ad2a53b-cd40-4c58-9145-39e8405174d5" />

New orders/Generate Bill:
<img width="985" height="606" alt="im3" src="https://github.com/user-attachments/assets/20f87ee8-73ec-451d-9bea-2344d5f5630e" />

Bill & Summary:
<img width="990" height="603" alt="im4" src="https://github.com/user-attachments/assets/476e19f7-22e9-48e5-a210-c14d40466f97" />
<img width="987" height="148" alt="im5" src="https://github.com/user-attachments/assets/031ed28b-5898-4418-b4f4-acfb46926eca" />

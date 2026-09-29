## Problem Statement

Many small cafes still write down customer orders and bills by hand. This takes a long time and can lead to mistakes, such as adding up the wrong total or forgetting an item. The staff also have to work out the GST amount themselves, which can cause errors when the cafe is busy. This project solves this problem by using a simple Python program to take the orders, work out the total, add GST and print a clear bill for the customer.

## Scope of the Project

This project is a command line billing system for a cafe. It lets a staff member enter the customer name and then pick items from a menu one at a time. The program keeps track of every item chosen, works out the cost, adds GST at 5 percent and prints a final bill. The project does not include things like online ordering, payment processing or saving bills to a file. It is meant to be a simple tool used on one computer at the till.

## Target Users

The main users of this program are cafe staff, such as cashiers or waiters, who take customer orders and prepare bills. It is best suited for small cafes that do not already have a proper billing machine or software, and want a quick, low cost way to manage orders and print bills.

## High Level Features

* Asks for the customer name before taking the order
* Shows a menu with fifteen food and drink items, each with a number and price
* Lets the user pick an item by number and enter how many they want
* Adds each item, its quantity and its cost to the order list
* Keeps a running total as items are added
* Lets the user finish the order and generate the final bill
* Prints a full bill showing the customer name, each item bought, the subtotal, GST at 5 percent and the grand total
* Ends with a thank you message for the customer
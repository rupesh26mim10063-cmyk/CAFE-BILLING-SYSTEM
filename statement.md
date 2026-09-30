# Problem Statement

Small cafes often write bills by hand or use a calculator. This is slow, and
mistakes happen while adding prices, calculating GST or applying discounts.
Sales records are also not saved, so the owner cannot easily see how much the
cafe earned.

This project is a simple Python program that lets the cafe staff take an
order, calculate the bill automatically and keep a record of all bills.

## Scope of the Project

- Console (command line) based program written in Python
- Managing the cafe menu (view, add, remove items)
- Taking a customer order with quantity
- Calculating subtotal, discount and 5% GST, and printing the bill
- Saving every bill in a text file and showing a sales summary
- Checking user input so the program does not crash
- Not included: online payment, database, graphical interface

## Target Users

- Cafe owners and cashiers of small cafes or canteens
- Students who want to understand a basic billing system

## High-Level Features

1. Menu management (view, add, remove items)
2. Order taking with quantity checking
3. Automatic bill with discount (10% on orders of Rs 500 or more) and GST
4. Bills saved in `bills.txt` and a sales summary report
5. Input validation and error handling
6. Unit tests for the main functions

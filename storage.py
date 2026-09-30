# storage.py
# Saves every bill in a text file and reads it back for the sales summary

from datetime import datetime

BILL_FILE = "bills.txt"


def save_bill(customer_name, total, filename=BILL_FILE):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    line = date_time + "," + customer_name + "," + str(total) + "\n"

    file = open(filename, "a")
    file.write(line)
    file.close()


def sales_summary(filename=BILL_FILE):
    # returns (number of bills, total sales)
    count = 0
    total_sales = 0.0

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        return 0, 0.0

    for line in file:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue          # skip broken lines
        try:
            total_sales += float(parts[2])
            count += 1
        except ValueError:
            continue

    file.close()
    return count, round(total_sales, 2)

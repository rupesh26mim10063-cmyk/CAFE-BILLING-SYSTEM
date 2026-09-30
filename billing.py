# billing.py
# Module 3: Billing (subtotal, discount, GST and printing the bill)

GST_RATE = 0.05          # 5% GST
DISCOUNT_LIMIT = 500     # discount only if subtotal is 500 or more
DISCOUNT_RATE = 0.10     # 10% discount


def calculate_bill(order):
    subtotal = 0
    for item in order:
        subtotal += item[3]

    discount = 0
    if subtotal >= DISCOUNT_LIMIT:
        discount = round(subtotal * DISCOUNT_RATE, 2)

    amount_after_discount = subtotal - discount
    gst = round(amount_after_discount * GST_RATE, 2)
    total = round(amount_after_discount + gst, 2)

    return subtotal, discount, gst, total


def print_bill(customer_name, order):
    subtotal, discount, gst, total = calculate_bill(order)

    print("\n----- FINAL BILL -----")
    print("Customer Name :", customer_name)

    for item in order:
        print(item[0], "x", item[1], " = ₹", item[3])

    print("Subtotal       : ₹", subtotal)
    print("Discount       : ₹", discount)
    print("GST (5%)       : ₹", gst)
    print("TOTAL          : ₹", total)
    print("Thank You! Visit Again")

    return total

# tests/test_cafe.py
# Simple unit tests for the cafe billing project
# Run from the main project folder with:  python -m unittest discover tests

import os
import sys
import unittest

# so that Python can find our modules in the parent folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import menu
import billing
import storage
from orders import add_to_order
from validation import is_valid_name, is_valid_quantity


class TestValidation(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_name("Rahul Sharma"))

    def test_empty_name(self):
        self.assertFalse(is_valid_name("   "))

    def test_name_with_numbers(self):
        self.assertFalse(is_valid_name("Rahul123"))

    def test_quantity_limits(self):
        self.assertTrue(is_valid_quantity(1))
        self.assertTrue(is_valid_quantity(50))
        self.assertFalse(is_valid_quantity(0))
        self.assertFalse(is_valid_quantity(51))


class TestMenu(unittest.TestCase):

    def test_get_existing_item(self):
        self.assertEqual(menu.get_item(1), ("Burger", 120))

    def test_get_missing_item(self):
        self.assertIsNone(menu.get_item(9999))

    def test_add_and_remove_item(self):
        number = menu.add_item("Test Cake", 99)
        self.assertEqual(menu.get_item(number), ("Test Cake", 99))
        self.assertTrue(menu.remove_item(number))
        self.assertIsNone(menu.get_item(number))

    def test_remove_missing_item(self):
        self.assertFalse(menu.remove_item(9999))


class TestOrders(unittest.TestCase):

    def test_add_to_order(self):
        order = []
        amount = add_to_order(order, "Burger", 120, 2)
        self.assertEqual(amount, 240)
        self.assertEqual(order[0], ("Burger", 2, 120, 240))


class TestBilling(unittest.TestCase):

    def test_bill_without_discount(self):
        order = [("Burger", 2, 120, 240), ("Pizza", 1, 250, 250)]
        subtotal, discount, gst, total = billing.calculate_bill(order)
        self.assertEqual(subtotal, 490)
        self.assertEqual(discount, 0)
        self.assertEqual(gst, 24.5)
        self.assertEqual(total, 514.5)

    def test_bill_with_discount(self):
        order = [("Pizza", 2, 250, 500)]
        subtotal, discount, gst, total = billing.calculate_bill(order)
        self.assertEqual(discount, 50)
        self.assertEqual(gst, 22.5)
        self.assertEqual(total, 472.5)

    def test_empty_order(self):
        result = billing.calculate_bill([])
        self.assertEqual(result, (0, 0, 0, 0))


class TestStorage(unittest.TestCase):

    test_file = "test_bills.txt"

    def tearDown(self):
        # delete the test file after every test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_summary_when_no_file(self):
        self.assertEqual(storage.sales_summary(self.test_file), (0, 0.0))

    def test_save_and_read_bills(self):
        storage.save_bill("Amit", 100.5, self.test_file)
        storage.save_bill("Neha", 200, self.test_file)
        count, total = storage.sales_summary(self.test_file)
        self.assertEqual(count, 2)
        self.assertEqual(total, 300.5)


if __name__ == "__main__":
    unittest.main()

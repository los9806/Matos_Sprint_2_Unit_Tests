import unittest
from cinos_units import Drink, Order

class TestOrder(unittest.TestCase):
    def test_get_items(self):
        order = Order()
        self.assertEqual(order.get_items(), [])  # Default is empty list

        drink = Drink(size="small")
        order.add_item(drink)
        self.assertEqual(order.get_items(), [drink])

    def test_get_num_items(self):
        order = Order()
        self.assertEqual(order.get_num_items(), 0)  # No items initially

        drink1 = Drink(size="medium")
        drink2 = Drink(size="large")
        order.add_item(drink1)
        order.add_item(drink2)
        self.assertEqual(order.get_num_items(), 2)

    def test_get_total(self):
        order = Order()
        drink1 = Drink(size="small")
        drink2 = Drink(size="large")
        order.add_item(drink1)
        order.add_item(drink2)
        self.assertAlmostEqual(order.get_total(), drink1.get_total() + drink2.get_total(), places=2)

    def test_get_tax(self):
        order = Order()
        drink = Drink(size="medium")
        order.add_item(drink)
        expected_tax = order.get_total() * 0.0725
        self.assertAlmostEqual(order.get_tax() - order.get_total(), expected_tax, places=2)

    def test_get_receipt(self):
        order = Order()
        drink1 = Drink(size="small")
        drink1.add_flavor("lime")
        drink2 = Drink(size="mega")
        order.add_item(drink1)
        order.add_item(drink2)

        receipt = order.get_receipt()
        self.assertEqual(receipt["number_drinks"], 2)
        self.assertEqual(receipt["subtotal"], order.get_total())
        self.assertAlmostEqual(receipt["tax"], order.get_total() * 0.0725, places=2)
        self.assertAlmostEqual(receipt["grand_total"], receipt["subtotal"] + receipt["tax"], places=2)


if __name__ == "__main__":
    unittest.main()
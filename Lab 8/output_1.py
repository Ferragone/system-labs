class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Order:
    def __init__(self, customer, product, quantity, shipping_address):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.shipping_address = shipping_address

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.shipping_address}")

    def calculate_shipping_cost(self):
        address = self.shipping_address
        if "New York" in address:
            return 5.00
        elif "California" in address:
            return 10.00
        else:
            return 15.00
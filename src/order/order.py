import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class Order:
    keys = ["customer_name", "customer_address",
            "customer_phone", "courier", "status", "items"]

    def __init__(self, customer_name: str, customer_address, customer_phone, courier, status, items):
        if customer_name.isnumeric():
            raise TypeError("Name must not be numeric")
        else:
            self.customer_name = customer_name
            self.customer_address = customer_address
            self.customer_phone = customer_phone
            self.courier = courier
            self.status = status
            self.items = items

    @classmethod
    def dict_to_obj(cls, order_dict: dict):
        try:
            order = Order(order_dict["customer_name"],
                          order_dict["customer_address"],
                          order_dict["customer_phone"],
                          order_dict["courier"],
                          order_dict["status"],
                          order_dict["items"])
        except KeyError:
            return -1
        return order

    @classmethod
    def create_order_from_user_input(cls):
        while True:
            try:
                order = Order(input("Customer name: "),
                              input("customer address: "),
                              input("Customer phone: "),
                              input("Courier index: "),
                              input("Status"),
                              input("Items: ")
                              )
                return order
            except:
                print("Invalid input - Try again!!")
                continue

    @classmethod
    def get_validated_update_details(cls, order_details):
        for k, v in order_details.items():
            if k == "customer_name":
                if v.isnumeric():
                    raise TypeError("Invalid name - try again")
            elif k == "customer_phone":
                if not v.isnumeric():
                    raise TypeError("Invalid phone number - try again")

        return order_details

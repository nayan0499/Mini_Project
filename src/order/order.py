import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))



class Order:

    keys = ["customer_name", "customer_address",
            "customer_phone", "courier", "status", "items"]

    status_list = ["preparing", "sent"]

    def __init__(self, customer_name, customer_address, customer_phone, courier, status,items,):
        if customer_name.isnumeric() and len(customer_name)> 2:
            raise TypeError("Name must not be numeric")
        else:
            self.customer_name = customer_name
            self.customer_address = customer_address
            self.customer_phone = customer_phone
            self.courier = courier
            self.status = status
            self.items = items




    @classmethod
    def create(cls):
        while True:
            try:
                order = Order(input("Customer name: "),
                              input("customer address: "),
                              input("Customer phone: "),
                              input("Courier index: "),
                              "preparing",
                              input("Items: ")
                              )
                return order
            except:
                print("Invalid input - Try again!!")
                continue
    
    @classmethod
    def get_update(cls, *args):
        status = {}
        if len(args) != 0:
            for x in args:
                status["status"] = input("New status: ")
            return status

        else: 
            order_details = {}
            for key in cls.keys: 
                input_by_user =  input(f"{key}: ")
                if input_by_user!= "":
                    order_details[key] = input_by_user
            try: 
                order_details = cls.get_validated_update(order_details)
                return order_details
            except TypeError as e: 
                print(e)
                return cls.get_update()


    @classmethod
    def get_validated_update(cls, order_details):
        for k,v in order_details.items():
            if k =="customer_name": 
                if v.isnumeric(): 
                    raise TypeError("Invalid name - Try again")
            elif k == "customer_phone":
                if not v.isnumeric(): 
                    raise TypeError("Invalid phone number - Try again")
        

        return order_details 

    @classmethod
    def dict_to_obj(cls, dict):
            order = Order(dict["customer_name"],
                        dict["customer_address"],
                        dict["customer_phone"],
                        dict["courier"],
                        dict["status"],
                        dict["items"]
                        )
            return order


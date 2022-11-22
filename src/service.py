from tabulate import tabulate
from src.order.order import Order
from src.product.product import Product
from src.courier.courier import Courier

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def get_valid_index_from_user(len_of_items: int):
    max_index = len_of_items - 1
    print(f"Select from 0 to {max_index}")
    try:
        index = int(input("Index: "))
        if index >= len_of_items:
            print("Invalid input")
            return get_valid_index_from_user(len_of_items)
    except:
        print("Invalid input")
        return get_valid_index_from_user(len_of_items)
    if index not in range(len_of_items) or index == "":
        return get_valid_index_from_user(len_of_items)
    else:
        return int(index)


def get_update_details(keys: list, *args) -> dict:
    status = {}
    for key in args:
        if key == "status":
            status[key] = input("New status: ")
        return status
    update_details = {}
    for key in keys:
        input_by_user = input(f"{key}: ")
        if input_by_user != "":
            update_details[key] = input_by_user
    return update_details


def convert_list_of_objects_into_table(list_of_objects: list):
    # if not isinstance(list_of_objects, object):
    #     raise TypeError
    item_list = []

    for product in list_of_objects:
        keys = [k.title() for k in product.__dict__.keys()]
        item_list.append([v for k, v in product.__dict__.items()])
    for i, item in enumerate(item_list):
        item.insert(0, i)
    table = tabulate(item_list, headers=keys, floatfmt=".1f", tablefmt="pipe")
    return table


def create_item_depending_on_object_type(object_type: str):
    if object_type == "product":
        item = Product.create_product_from_user_input()
        return item
    elif object_type == "courier":
        item = Courier.create_courier_from_user_input()
        return item
    elif object_type == "order":
        item = Order.create_order_from_user_input()
        return item


def get_update_details_from_user_input(item_type: str, *args) -> dict:
    if item_type == "product":
        update_details = get_update_details(Product.keys, *args)
        validated_update_details = Product.get_validated_update_details(update_details)
        return validated_update_details
    elif item_type == "courier":
        update_details = get_update_details(Courier.keys, *args)
        validated_update_details = Courier.get_validated_update_details(update_details)
        return validated_update_details
    elif item_type == "order":
        update_details = get_update_details(Order.keys, *args)
        update_details = Order.get_validated_update_details(update_details)
        return update_details


def display(repo):
    list_of_objects = repo.get()

    if len(list_of_objects) == 0:
        print("No items to display")
    else:
        table = convert_list_of_objects_into_table(list_of_objects)
        print(table)


def add(item, repo):
    return repo.add(item)


def update(index, updated_details, repo):
    return repo.update(index, updated_details)


def delete(index, repo):
    return repo.delete(index)


def save(repo):
    return repo.save()

# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# from src.csvhandler.csv import load_from_file, save_to_file
# from src.order.order import Order
# from src.courier.courier import Courier
# from src.courier.csv_courier_repo import CourierRepo
# from src.product.csv_product_repo import ProductRepo
# from order.csv_order_repo import OrderRepo
# from src.product.product import Product
# from tabulate import tabulate


# def get_update_details():
#     pass


# class Service: 

#     def __init__(self, repo, item_type):
#         self.repo = repo
#         self.keys = item_type.keys  
#         self.item_type = item_type

#     def get_valid_index_from_user(self):
#         num_of_items = len(self.repo.get()) -1 
#         print(f"Select from 0 to {num_of_items}")
#         try: 
#             index = int(input("Index: "))
#         except: 
#             return self.get_valid_index_from_user()
#         if index not in range(num_of_items + 1) or index == "":
#             return self.get_valid_index_from_user()
#         return int(index)

#     def display(self):
#         objects= self.repo.get()
#         if len(objects) == 0:
#             print("No items to display")
#         else: 
#             item_list = []
#             for object in objects: 
#                 item = self.item_type.object_to_list(object)
#                 item_list.append(item)
#             print(tabulate(item_list, headers=self.keys))


#     def add(self):
#         item = self.item_type.create_item_from_user_input()
#         self.repo.add(item)
#         return item 

#     def get_update_details(self,keys):
#         updated_values = {}
#         for k in keys:
#             updated_values[k] = input(f"{k}: ")
#         return updated_values

#     def update(self,index, keys):
#         updated_details = self.get_update_details(keys)
#         try: 
#             self.repo.update(index, updated_details) #TODO: change this to **kwargs
#         except:
#             return self.update()
#         # return updated_details

#     def delete(self,index):
#         self.repo.delete(index)
#         return index 

#     def save(self):
#         self.repo.save()


# prod_repo = ProductRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\product.csv")
# product_manager = Service(prod_repo, Product)

# courier_repo = CourierRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\courier.csv")
# courier_manager= Service(courier_repo, Courier)

# order_repo = OrderRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\order.csv")
# order_manager = Service(order_repo, Order)

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


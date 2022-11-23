import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tabulate import tabulate

from src.courier.courier import Courier
from src.order.order import Order
from src.courier.courier_repository import CourierFileRepository
from src.order.order_repository import OrderFileRepository
from src.product.product import Product
from src.product.product_repository import ProductFileRepository


class Service:
    def __init__(self, repo, item_type):
        self.repo = repo
        self.item_type = item_type
    
    def display(self):
        list_of_items = self.repo.get()
        if len(list_of_items) == 0:
            print('No items to display')
        else:
            table = self.tabulate_list(list_of_items, False)
            print(table)

    def add(self):
        item = self.item_type.create()
        self.repo.add(item)
        return item

    def update(self, *args):
        list_of_items = self.repo.get()
        print(self.tabulate_list(list_of_items, True))
        index = self.get_index(len(list_of_items))
        updated_details = self.item_type.get_update(*args)
        self.repo.update(index, updated_details)
        return updated_details

    def delete(self):
        list_of_items = self.repo.get()
        print(self.tabulate_list(list_of_items, True))
        index = self.get_index(len(list_of_items))
        self.repo.delete(index)
        return index

    def save(self):
        self.repo.save()




    def get_index(self, len_of_items: int):
        max_index = len_of_items - 1
        print(f'Select from 0 to {max_index}')
        try:
            index = int(input('Index: '))
            if index > len_of_items:
                print('Invalid input')
                return self.get_index(len_of_items)
        except:
            print('Invalid input')
            return self.get_index(len_of_items)
        if index not in range(len_of_items) or index == '':
            return self.get_index(len_of_items)
        else:
            return int(index)

    def tabulate_list(
        self, list_of_objects: list, with_index=True
    ):
        item_list = []
        for product in list_of_objects:
            keys = [k.title() for k in product.__dict__.keys()]
            item_list.append([v for k, v in product.__dict__.items()])
        if with_index:
            for i, item in enumerate(item_list):
                item.insert(0, i)
            keys.insert(0, 'Index')
        table = tabulate(
            item_list, headers=keys, floatfmt='.1f', tablefmt='pipe'
        )
        return table

   


prod_repo = ProductFileRepository(
    r'C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\product.csv'
)
product_service = Service(prod_repo, Product)

courier_repo = CourierFileRepository(
    r'C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\courier.csv'
)
courier_service = Service(courier_repo, Courier)

order_repo = OrderFileRepository(
    r'C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\order.csv'
)
order_service = Service(order_repo, Order)

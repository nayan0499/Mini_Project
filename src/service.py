import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.product.product import Product
from order.order import Order
from courier.courier import Courier
from courier.csv_courier_repo import CourierRepo
from product.product_repo import ProductRepo
from order.csv_order_repo import OrderRepo
from tabulate import tabulate



class Service: 

    def __init__(self, repo, item_type):
        self.repo = repo
        # self.keys = item_type.keys  
        self.item_type = item_type 
        
    def get_valid_index_from_user(self,len_of_items: int):
        max_index = len_of_items-1
        print(f"Select from 0 to {max_index}")
        try:
            index = int(input("Index: "))
            if index > len_of_items:
                print("Invalid input")
                return self.get_valid_index_from_user(len_of_items)
        except:
            print("Invalid input")
            return self.get_valid_index_from_user(len_of_items)
        if index not in range(len_of_items) or index == "":
            return self.get_valid_index_from_user(len_of_items)
        else:
            return int(index)


    def convert_list_of_items_into_table(self,list_of_objects: list):
        item_list = []

        for product in list_of_objects:
            keys = [k.title() for k in product.__dict__.keys()]
            item_list.append([v for k, v in product.__dict__.items()])
        for i, item in enumerate(item_list):
            item.insert(0, i)
        table = tabulate(item_list, headers=keys, floatfmt=".1f", tablefmt="pipe")
        return table

    def display(self):
        list_of_items = self.repo.get()
        if len(list_of_items) == 0:
            print("No items to display")
        else:
            table = self.convert_list_of_items_into_table(list_of_items)
            print(table)


    def add(self):
        item = self.item_type.create_item_from_user_input()
        self.repo.add(item)
        return item 

    def update(self,*args):
        index = self.get_valid_index_from_user(len(self.repo.get()))
        updated_details = self.item_type.get_update_details(*args)
        self.repo.update(index, updated_details) 
        return updated_details

    def delete(self):
        index = self.get_valid_index_from_user(len(self.repo.get()))
        self.repo.delete(index)
        return index 

    def save(self):
        self.repo.save()
    


prod_repo = ProductRepo(r"C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\product.csv")
product_manager = Service(prod_repo, Product)

courier_repo = CourierRepo(r"C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\courier.csv")
courier_manager= Service(courier_repo, Courier)

order_repo = OrderRepo(r"C:\Users\NayanGurung\Generation\week6\1_mini_project_most_refactored\src\data\order.csv")
order_manager = Service(order_repo, Order)




        
        

    

    
              
    



        


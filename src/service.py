import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.product.product import Product
from order.order import Order
from courier.courier import Courier
from courier.csv_courier_repo import CourierRepo
from product.csv_product_repo import ProductRepo
from order.csv_order_repo import OrderRepo
from tabulate import tabulate





class Service: 

    def __init__(self, repo, item_type):
        self.repo = repo
        self.keys = item_type.keys  
        self.item_type = item_type

    def get_valid_index_from_user(self):
        num_of_items = len(self.repo.get()) -1 
        print(f"Select from 0 to {num_of_items}")
        try: 
            index = int(input("Index: "))
        except: 
            return self.get_valid_index_from_user()
        if index not in range(num_of_items + 1) or index == "":
            return self.get_valid_index_from_user()
        return int(index)

    def display(self):
        objects= self.repo.get()
        if len(objects) == 0:
            print("No items to display")
        else: 
            item_list = []
            for object in objects: 
                item = self.item_type.object_to_list(object)
                item_list.append(item)
            print(tabulate(item_list, headers=self.keys)) 


    def add(self):
        item = self.item_type.create_item_from_user_input()
        self.repo.add(item)
        return item 

    def update(self,index, *args):
        updated_details = self.item_type.get_update_details(*args)
        self.repo.update(index, updated_details) #TODO: change this to **kwargs
        return updated_details

    def delete(self,index):
        self.repo.delete(index)
        return index 

    def save(self):
        self.repo.save()
    


prod_repo = ProductRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\product.csv")
product_manager = Service(prod_repo, Product)

courier_repo = CourierRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\courier.csv")
courier_manager= Service(courier_repo, Courier)

order_repo = OrderRepo(r"C:\Users\NayanGurung\Generation\week6\recent_mini_project\src\data\order.csv")
order_manager = Service(order_repo, Order)




        
        

    

    
              
    



        


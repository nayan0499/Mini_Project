import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from csvhandler.csv import load_from_file, save_to_file
from order.order_abstract import OrderAbstract
from order.order import Order

class OrderRepo(OrderAbstract): 

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.list = load_from_file(file_name, Order)
    
    def add(self, order):
        self.list.append(order)
    

    def update(self, index, updated_order):
        selected_order = self.list[index]
        for k,v in updated_order.items():
            if k == "customer_name":
                selected_order.customer_name = v
            elif k == "customer_address": 
                selected_order.customer_address= v
            elif k == "customer_phone": 
                selected_order.customer_phone= v
            elif k == "courier": 
                selected_order.courier= v
            elif k == "status": 
                selected_order.status= v
            elif k == "items": 
                selected_order.items= v
    
    def delete(self, index):
        self.list.pop(index)

    def get(self):
        return self.list
    
    def save(self):
        save_to_file(self.list, self.file_name, Order.keys)
    
        


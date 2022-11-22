
import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from csvhandler.csv import load_from_file, save_to_file
from product.product_abstract import ProductAbstract
from src.product.product import Product
from src.repository.repository import Repository

class ProductFileRepository(Repository): 

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.list = load_from_file(file_name, Product)
    
    def add(self, product):
        self.list.append(product)

    def update(self, index, updated_product):
        selected_product = self.list[index]
        for k,v in updated_product.items():
            if k == "name":
                selected_product.name = v
            elif k == "price": 
                selected_product.price = v

    def delete(self, index):
        self.list.pop(index)

    def get(self):
        return self.list
    
    def save(self):
        save_to_file(self.list, self.file_name, Product.keys)

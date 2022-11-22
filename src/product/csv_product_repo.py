from src.csvhandler.csv import load_from_file, save_to_file
from src.product.product_abstract import ProductAbstract
from src.product.product import Product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class ProductRepo(ProductAbstract):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.list = load_from_file(file_name, Product)

    def add(self, product):
        self.list.append(product)
        return 1

    def update(self, index, updated_product):
        selected_product = self.list[index]
        for k, v in updated_product.items():
            if k == "name":
                selected_product.name = v
            elif k == "price":
                selected_product.price = v
        return 1

    def delete(self, index):
        self.list.pop(index)
        return 1

    def get(self):
        return self.list

    def save(self):
        save_to_file(self.list, self.file_name, Product.keys)
        return 1


prod_repo = ProductRepo(r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\src\data\product.csv")

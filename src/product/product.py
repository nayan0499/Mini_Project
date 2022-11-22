import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class Product:
    keys = ["name", "price"]

    def __init__(self, name: str, price: float):
        if name.isnumeric():
            raise TypeError("Name must not be numeric")
        elif not isinstance(price, float):
            try:
                price = float(price)
            except:
                raise TypeError("Price must not contain letters")
        if price < 0.0:
            raise ValueError("Price must be greater than 0")
        else:
            self.price = price
            self.name = name.title()

    @classmethod
    def dict_to_obj(cls, prod_dict: dict):
        try:
            product = Product(prod_dict["name"], float(prod_dict["price"]))
            return product
        except KeyError:
            return -1

    @classmethod
    def create_product_from_user_input(self):
        while True:
            try:
                new_product = Product(
                    input("Product name: ").title(),
                    float(input("Product price: "))
                )
                return new_product
            except ValueError:
                print("price must be a float")
                continue

            except TypeError as x:
                print(x)
                continue

    @classmethod
    def get_validated_update_details(cls, product_details):
        for k, v in product_details.items():
            if k == "name":
                if v.isnumeric():
                    raise TypeError("Invalid name- try again")
                else:
                    product_details[k] = v.title()
            elif k == "price":
                try:
                    product_details[k] = float(v)
                except:
                    raise TypeError("price must only contain numbers -try again")

        return product_details

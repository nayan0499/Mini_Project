import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class Product:

    keys = ['name', 'price']

    def __init__(self, name: str, price: float):
        if name.isnumeric():
            raise TypeError('Name must not be numeric')
        elif price < 0.0:
            raise TypeError('Price must be greater than 0')
        else:
            self.price = price
            self.name = name.title()

    @classmethod
    def dict_to_obj(cls, dict):
        try:
            product = Product(dict['name'], float(dict['price']))
            return product
        except KeyError:
            return -1

    @classmethod
    def create(cls):
        while True:
            try:
                new_product = Product(
                    input('Product name: ').title(),
                    float(input('Product price: ')),
                )
                return new_product
            except ValueError:
                print('price must be a float')
                continue

            except TypeError as x:
                print(x)
                continue

    @classmethod
    def get_update(cls):

        product_details = {}
        for key in cls.keys:
            input_by_user = input(f'{key}: ')
            if input_by_user != '':
                product_details[key] = input_by_user
        try:
            product_details = cls.get_validated_update(product_details)
            return product_details
        except TypeError as e:
            print(e)   # TODO:
            return cls.get_update_details()

    @classmethod
    def get_validated_update(cls, product_details):
        for k, v in product_details.items():
            if k == 'name':
                if v.isnumeric():
                    raise TypeError('Invalid name- try again')
                else:
                    product_details[k] = v.title()
            elif k == 'price':
                try:
                    product_details[k] = float(v)
                except:
                    raise TypeError(
                        'price must only contain numbers -try again'
                    )

        return product_details

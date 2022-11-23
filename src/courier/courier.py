import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))



class Courier:
    keys = ["name", "phone"]

    def __init__(self, name, phone):
        if name.isnumeric():
            raise TypeError("Name must not be numeric")
        elif not phone.isnumeric():
            raise TypeError("Phone must only contain numbers")
        else:
            self.name = name
            self.phone = phone

    

    @classmethod
    def dict_to_obj(cls, dict):
    
        courier = Courier(dict["name"], dict["phone"])
        return courier

    @classmethod
    def create(cls):
        while True:
            try:
                courier = cls(input("Courier name: "),
                              (input("Phone number: ")))
                return courier
            except TypeError as e:
                print(e)
                continue



    @classmethod
    def get_update(cls):
        courier_details = {}
        for key in cls.keys: 
            input_by_user =  input(f"{key}: ")
            if input_by_user!= "":
                courier_details[key] = input_by_user
        try: 
            courier_details = cls.get_validated_update(courier_details)
            return courier_details
        except TypeError as e: 
            print(e)
            return cls.get_update()


    @classmethod
    def get_validated_update(cls, product_details):
        for k,v in product_details.items():
            if k =="name": 
                if v.isnumeric(): 
                    raise TypeError("name is invalid - try again")
                else: 
                    product_details[k] = v.title()
            elif k == "phone":
                if not v.isnumeric(): 
                    raise TypeError("phone is invalid - try again")
                else: 
                    product_details[k] = v
            
        return product_details



   






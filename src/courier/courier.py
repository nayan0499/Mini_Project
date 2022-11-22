import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class Courier:
    keys = ["name", "phone"]

    def __init__(self, name, phone):
        if name.isnumeric():
            raise TypeError("Name must not be numeric")
        elif not phone.isnumeric():
            raise TypeError("Phone must not contain letters")
        else:
            self.name = name
            self.phone = phone

    @classmethod
    def dict_to_obj(cls, courier_dict: dict):
        print(type(courier_dict))
        if not isinstance(courier_dict, dict):
            raise TypeError("The argument be a dictionary")
        try:
            courier = Courier(courier_dict["name"], courier_dict["phone"])
            return courier
        except KeyError:
            print("The dictionary provided does not contain the required keys ")
            return -1

    @classmethod
    def create_courier_from_user_input(cls):
        while True:
            try:
                courier = cls(input("Courier name: "),
                              (input("Phone number: ")))
                return courier
            except TypeError as e:
                print(e)
                continue

    @classmethod
    def get_validated_update_details(cls, courier_details):
        for k, v in courier_details.items():
            if k == "name":
                if v.isnumeric():
                    raise TypeError("Invalid name - Try again")
                else:
                    courier_details[k] = v.title()
            elif k == "phone":
                if not v.isnumeric():
                    raise TypeError("Invalid phone number - Try again")
                else:
                    courier_details[k] = v

        return courier_details

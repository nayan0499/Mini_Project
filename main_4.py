import csv 

def load_from_file(name,item_type):
    name += "s"
    list=[]
    with open(f"{name}.csv", "r") as file: 
        csv_file = csv.DictReader(file)
        for row in csv_file: 
            obj = item_type.dict_to_obj(row)
            list.append(obj)
        return list

class Menu:

    def __init__(self, name, options):
        self.name = name
        self.num_of_options = len(options)
        self.options = options 
        self.selected = "n/a"

    def get_menu(self): 
        capitalised_name = self.name.upper()
        menu = "\n~~~~~~~~~~~~~~~~~~~ {} MENU ~~~~~~~~~~~~~~~~~~~~~~\n".format(capitalised_name)
        for index,option in enumerate(self.options): 
            s = (29-len(option))* "-" 
            menu+= "{0} {1} {2}\n".format(index,s,option)
        return menu 

    def set_selected_option(self, selected_option):
        try: 
            selected_option = int(selected_option)
        except ValueError: 
            print(f"Invalid number - Select from 0 to {self.num_of_options}")
            return -1
        while True: 
            if selected_option not in range(self.num_of_options):
                return "Invalid option - Select again!"
            else:
                self.selected = selected_option
                return selected_option

                 

main_menu = Menu("Main", ["Save any changes & Exit", "View the product menu", "View the courier menu","View the order menu" ])
product_menu = Menu("Product",["Return to the main menu","View all products", "Add a new product", "Update an existing product", "Delete a product"])
order_menu = Menu("Order", ["Return to the main menu","View all orders", "Create a new order","Update the order status","Update an existing order","Delete an order"])
courier_menu = Menu("Courier", ["Return to the main menu", "View all couriers","Add a new courier","Update an existing courier", "Delete a courier"])      


    
class Product: 

    def __init__(self, name, price):
        if name.isnumeric():
            raise TypeError("Name must not be numeric")
        elif price < 0: 
            raise TypeError("Price must be greater than 0")
        else:
            self.price = price
            self.name = name

    def __eq__(self, other):
        return self.price == other.price and self.name == other.name

    @classmethod
    def keys(cls):
        return ["name", "price"]
    @classmethod
    def from_user_input(cls): #TODO: Make it more testable 
        while True: 
            try: 
                new_product = cls(
                input("Product name: "),
                float(input("Product price: "))
                )
                return new_product   
            except ValueError as e: 
                print(e)
                continue
            except TypeError as x:
                print(x)
                continue
   
    def key_and_function_dict(self):
        return {
            "name": self.name,
            "price": self.price
        }

    def update_details(self): 
        while True: 
            try: 
                for key in self.keys(): 
                    input_by_user = input(f"new {key}: ")
                    if input_by_user != "":
                        if key == "name":
                            self.name = input_by_user
                        elif key == "price":
                            self.price = float(input_by_user)
                break
            except ValueError as ve: 
                print(ve)
                continue
            except TypeError as te:
                print(te)
                continue 


    def display(self):
        s = (29-len(self.name))* "-" 
        return f"{self.name} {s} {self.price}"
    

    @classmethod
    def dict_to_obj(cls,dict):
        product = Product(dict["name"], float(dict["price"]))
        return product
            


class Courier: 

    def __init__(self, name, phone):
        if name.isnumeric():
            raise TypeError("Name must not be numeric")
        elif not isinstance(phone,int):
            raise TypeError("Phone must be int")
        else:
            self.name = name 
            self.phone= phone  

    @classmethod
    def keys(self):
        return ["name","phone"]
    
    def display(self):
        return f"{self.name}       {self.phone}"


    @classmethod
    def from_user_input(cls):
        while True: 
            try: 
                courier = cls(name = input("Courier name: "), phone= int(input("Phone number: ")) )
                return courier
            except: 
                print("Invalid input - Try again!!")
                continue
    
    def update_details(self):
        keys = ["name","phone"]
        for key in keys: 
            input_by_user = input(f"new {key}: ")
            if input_by_user != "":
                if key == "name":
                    self.name = input_by_user
                elif key == "phone":
                    self.phone = int(input_by_user)
    @classmethod
    def dict_to_obj(cls,dict):
        courier= Courier(dict["name"],int(dict["phone"]) )
        return courier



class Order: 
    def __init__(self,customer_name, customer_address, customer_phone, courier, status, items ):
        self.customer_name= customer_name
        self.customer_address =customer_address
        self.customer_phone = customer_phone
        self.courier = courier
        self.status = status
        self.items = items


    def display(self):
        return f"{self.customer_name}        {self.customer_address}           {self.customer_phone}              {self.courier}          {self.status}       {self.items}"


    @classmethod
    def keys(self):
        return ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]


    @classmethod
    def from_user_input(cls):
        while True: 
            # try: 
                order = Order(customer_name = input("Customer name: "), 
                              customer_address= input("customer address: "), 
                              customer_phone= input("Customer phone: "), 
                              courier= input("Courier index: "), 
                              status = input("Status"), 
                              items = input("Items: ")
                            )
                return order
            # except: 
            #     print("Invalid input - Try again!!")
            #     continue

    
    def update_details(self, *args):
        if len(args) != 0: 
            for x in args: 
                if x == "status": 
                    input_by_user = input("new status: ")
                    self.status = input_by_user
        else:
                keys =Order.keys()
                ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
                for key in keys: 
                    input_by_user = input(f"new {key}: ")
                    if input_by_user != "":
                        if key == "customer_address":
                            self.customer_address = input_by_user
                        elif key == "customer_phone":
                            self.customer_phone = input_by_user
                        elif key == "customer_name":
                            self.customer_name = input_by_user
                        elif key == "courier":
                            self.courier = input_by_user
                        elif key == "status":
                            self.status = input_by_user
                        else:
                            self.items = input_by_user


    @classmethod
    def dict_to_obj(cls,dict):
        order= Order(dict["customer_name"], 
                    dict["customer_address"],
                    dict["customer_phone"], 
                    dict["courier"],
                    dict["status"],
                    dict["items"]  
                    )
        return order
 

class List:
    def __init__(self,list_name,item_type):
        self._list_name = list_name
        self._item_type = item_type
        self._items = load_from_file(list_name,item_type)
        self.size = len(self._items)
    
    def add(self):
        new_item = self._item_type.from_user_input()
        self._items.append(new_item)

    
    def update(self, *args):
        index = int(input("update index: "))
        if len(args) !=0: 
            for x in args: 
                self._items[index].update_details(x)
        else: 
            self._items[index].update_details()
    def delete(self):
        while True:
            index = int(input("Index: "))
            if index in range(len(self._items)):
                self._items.pop(index)
                break 
            else:
                print("Index invalid- Try again")

    
    def display(self):
        keys = self._item_type.keys()
        for key in keys: 
            print(key + "          ", end="")
        print("")
        for x in self._items:
            print(x.display())
         
        
    def save(self): 
        name = self._list_name + "s"
        with open(f'{name}.csv', 'w',newline='') as f:  # You will need 'wb' mode in Python 2.x
            w = csv.DictWriter(f, self._item_type.keys(), quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in self._items:
                w.writerow(x.__dict__)
                    



orders = List("order",Order)
couriers = List("courier", Courier)
products = List("product", Product)


def sub_app(sub_menu, list):
    while True:
        sub_menu_display = sub_menu.get_menu()
        print(sub_menu_display)

        selected_option = input("Select input: ")
        sub_menu.set_selected_option(selected_option)
        if sub_menu.selected == 0: 
            break
        elif sub_menu.selected == 1: 
          
            list.display()
        elif sub_menu.selected == 2: 
          
            list.add()
        elif sub_menu.selected==3 and list._item_type == Order:
            list.update("status")
        elif sub_menu.selected==3 and list._item_type != Order:
           
            list.update()
        elif sub_menu.selected==4 and list._item_type == Order:
          
            list.update()
        elif sub_menu.selected==4 and list._item_type != Order:
          
            list.delete()
        elif sub_menu.selected==5 and list._item_type == Order:
          
            list.delete()
        

def app():

    while True:

        main_menu_display = main_menu.get_menu()
        print(main_menu_display)

        while True: 
            selected_option = input("Select input: ")
            if selected_option != -1:
                break
            else: 
                print("Try again")

        main_menu.set_selected_option(selected_option)
        if main_menu.selected == 0:
            products.save()
            couriers.save()
            orders.save()
            break
        elif main_menu.selected == 1: 
            sub_app(product_menu, products)
        elif main_menu.selected == 2: 
            sub_app(courier_menu, couriers)
        elif main_menu.selected ==3: 
            sub_app(order_menu, orders)

app()



    








class Menu:
    def __init__(self, name, options):
        self.name = name
        self.num_of_options = len(options)
        self.options = options
        self.selected = "n/a"

    def get_menu(self):
        capitalised_name = self.name.upper()
        menu = "\n~~~~~~~~~~~~~~~~~~~ {} MENU ~~~~~~~~~~~~~~~~~~~~~~\n".format(
            capitalised_name)
        for index, option in enumerate(self.options):
            s = (29-len(option)) * "-"
            menu += "{0} {1} {2}\n".format(index, s, option)
        return menu

    def set_selected_option(self, selected_option):
        try:
            selected_option = int(selected_option)
        except ValueError:
            print(f"Invalid option selected - Option must not contain letters. Select from 0 to {self.num_of_options}")
            return -1
        if selected_option not in range(self.num_of_options):
            num_of_options = self.num_of_options-1
            print(f"Invalid option selected - Select from 0 to {num_of_options}")
            return -1
        else:
            self.selected = selected_option
            return selected_option





menu = Menu("Main", ["Save any changes & Exit", "View the product menu",
                "View the courier menu", "View the order menu"])
prod_menu = Menu("Product", ["Return to the main menu", "View all products",
                    "Add a new product", "Update an existing product", "Delete a product"])
ord_menu = Menu("Order", ["Return to the main menu", "View all orders", "Create a new order",
                "Update the order status", "Update an existing order", "Delete an order"])
cour_menu = Menu("Courier", ["Return to the main menu", "View all couriers",
                    "Add  new courier", "Update an existing courier", "Delete a courier"])
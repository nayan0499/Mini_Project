import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from menu import menu, prod_menu, ord_menu, cour_menu
from service import courier_manager, order_manager, product_manager



def sub_app(sub_menu, service_layer):
    while True:

        sub_menu_display = sub_menu.get_menu()
        print(sub_menu_display)
        selected_option = input("Select input: ")
        sub_menu.set_selected_option(selected_option)

        if sub_menu.selected == 0:
            break

        elif sub_menu.selected == 1:
            service_layer.display()

        elif sub_menu.selected == 2:
            service_layer.add()

        elif sub_menu.selected == 3 and sub_menu == ord_menu:
            index = service_layer.get_valid_index_from_user()
            service_layer.update(index, "status")

        elif sub_menu.selected == 3:
            index = service_layer.get_valid_index_from_user()
            service_layer.update(index)

        elif sub_menu.selected == 4 and sub_menu == ord_menu:
            index = service_layer.get_valid_index_from_user()
            service_layer.update(index)
        elif sub_menu.selected == 4:
            index = service_layer.get_valid_index_from_user()
            service_layer.delete(index)
        elif sub_menu.selected == 5 and sub_menu == ord_menu:
            index = service_layer.get_valid_index_from_user()
            service_layer.delete(index)


def app(main_menu, product_menu, courier_menu, order_menu, order_service, product_service, courier_service):
    
    while True:
        print(main_menu.get_menu())
        selected_option = input("Select input: ")
        main_menu.set_selected_option(selected_option)

        if main_menu.selected == 0:
            product_service.save()
            courier_service.save()
            order_service.save()
            break

        elif main_menu.selected == 1:
            sub_app(product_menu, product_service)
        elif main_menu.selected == 2:
            sub_app(courier_menu, courier_service)
        elif main_menu.selected == 3:
            sub_app(order_menu, order_service)


app(menu, prod_menu, cour_menu, ord_menu, order_manager, product_manager, courier_manager)
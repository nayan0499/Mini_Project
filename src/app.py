import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from menu.menu import menu, prod_menu, ord_menu, cour_menu
from src.product.csv_product_repo import prod_repo
from src.order.csv_order_repo import order_repo
from src.courier.csv_courier_repo import courier_repo
from service import *



def sub_app(sub_menu, repo):
    while True:

        sub_menu_display = sub_menu.get_menu()
        print(sub_menu_display)
        selected_option = input("Select input: ")
        sub_menu.set_selected_option(selected_option)

        if sub_menu.selected == 0:
            break

        elif sub_menu.selected == 1:
            display(repo)

        elif sub_menu.selected == 2:
            new_item = create_item_depending_on_object_type(sub_menu.name)
            add(new_item, repo)

        elif sub_menu.selected == 3 and sub_menu.name == "order":
            display(repo)
            index = get_valid_index_from_user(len(repo.get()))
            update_details = get_update_details_from_user_input(sub_menu.name, "status")
            update(index, update_details, repo)

        elif sub_menu.selected == 3:
            display(repo)
            index = get_valid_index_from_user(len(repo.get()))
            update_details = get_update_details_from_user_input(sub_menu.name)
            update(index, update_details, repo)

        elif sub_menu.selected == 4 and sub_menu == ord_menu:
            display(repo)
            index = get_valid_index_from_user(len(repo.get()))
            update_details = get_update_details_from_user_input(sub_menu.name)
            update(index, update_details, repo)

        elif sub_menu.selected == 4:
            display(repo)
            index = get_valid_index_from_user(len(repo.get()))
            delete(index, repo)

        elif sub_menu.selected == 5 and sub_menu == ord_menu:
            display(repo)
            index = get_valid_index_from_user(len(repo.get()))
            delete(index, repo)


def app(main_menu, product_menu, courier_menu, order_menu, order_repo_impl, prod_repo_impl, courier_repo_impl):
    while True:
        print(main_menu.get_menu())
        selected_option = input("Select input: ")
        main_menu.set_selected_option(selected_option)

        if main_menu.selected == 0:
            save(prod_repo_impl)
            save(courier_repo_impl)
            save(order_repo_impl)
            print("EXIT")
            break

        elif main_menu.selected == 1:
            sub_app(product_menu, prod_repo_impl)

        elif main_menu.selected == 2:
            sub_app(courier_menu, courier_repo_impl)

        elif main_menu.selected == 3:
            sub_app(order_menu, order_repo_impl)


app(menu, prod_menu, cour_menu, ord_menu, order_repo, prod_repo, courier_repo)

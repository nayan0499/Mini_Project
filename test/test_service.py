from src.service import *
from src.product.csv_product_repo import ProductRepo
from unittest.mock import patch, call, Mock
from mock import MagicMock
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@patch("builtins.input", return_value="1")
def test_get_valid_index_from_user(mock_input):
    len_of_items = 2
    actual = get_valid_index_from_user(len_of_items)
    expected = 1
    assert actual == expected


@patch("builtins.input", side_effect=["4", "1"])
def test_get_valid_index_from_user_with_invalid_index(mock_input):
    len_of_items = 3
    actual = get_valid_index_from_user(len_of_items)
    expected = 1
    assert actual == expected


@patch("builtins.input", side_effect=["", "1"])
def test_get_valid_index_from_user_when_empty_input(mock_input):
    len_of_items = 3
    actual = get_valid_index_from_user(len_of_items)
    expected = 1
    assert actual == expected


@patch("builtins.input", side_effect=["e", "1"])
def test_get_valid_index_from_user_with_invalid_input(mock_input):
    len_of_items = 3
    actual = get_valid_index_from_user(len_of_items)
    expected = 1
    assert actual == expected
    mock_input.assert_has_calls([call("Index: "), call("Index: ")])


@patch("builtins.input", side_effect=["Coke", "1.1"])
def test_get_update_details_without_args(mock_input):
    keys = ["name", "price"]
    actual = get_update_details(keys)
    expected = {"name": "Coke", "price": "1.1"}
    assert actual == expected


@patch("builtins.input", return_value="sent")
def test_get_update_details_with_args(mock_input):
    keys = ["name", "price"]
    actual = get_update_details(keys, "status")
    expected = {"status": "sent"}
    assert actual == expected


@patch("builtins.input", side_effect=["", "1.1"])
def test_get_update_details_with_updated_price(mock_input):
    keys = ["name", "price"]
    actual = get_update_details(keys)
    expected = {"price": "1.1"}
    assert actual == expected


@patch("src.product.product.Product.create_product_from_user_input", return_value=Product("Coke", 1.1))
def test_create_item_depending_on_item_type(mock_product):
    actual = create_item_depending_on_object_type("product")
    assert type(actual) is Product
    assert mock_product.is_called_once()


@patch("src.product.product.Product.create_product_from_user_input", return_value=Product("Coke", 1.1))
def test_create_instance_when_item_type_is_product(mock_product):
    actual = create_item_depending_on_object_type("product")
    assert type(actual) is Product
    assert mock_product.is_called_once()


@patch("src.courier.courier.Courier.create_courier_from_user_input", return_value=Courier("Jane", "07450989860"))
def test_create_instance_when_item_type_is_courier(mock_courier):
    actual = create_item_depending_on_object_type("courier")
    assert type(actual) is Courier
    assert mock_courier.is_called_once()


@patch("src.order.order.Order.create_order_from_user_input", return_value=Product("Coke", 1.1))
def test_create_item_depending_on_item_type_is_order(mock_product):
    actual = create_item_depending_on_object_type("order")
    assert type(actual) is Product
    assert mock_product.is_called_once()


@patch("src.service.get_update_details", return_value={"name": "Coke", "price": "1.1"})
@patch("src.product.product.Product.get_validated_update_details", return_value={"name": "Coke", "price": 1.1})
def test_get_update_details_from_user_input(mock_validated_update_details, mock_update_details):
    expected = {"name": "Coke", "price": 1.1}
    actual = get_update_details_from_user_input("product")
    assert actual == expected


@patch("src.service.get_update_details", return_value={"name": "Jane", "phone": "07450989860"})
@patch("src.courier.courier.Courier.get_validated_update_details",
       return_value={"name": "Jane", "phone": "07450989860"})
def test_get_update_details_from_user_input(mock_validated_update_details, mock_update_details):
    expected = {"name": "Jane", "phone": "07450989860"}
    actual = get_update_details_from_user_input("courier")
    assert actual == expected


# @patch("src.service.convert_list_of_objects_into_table", return_value = "")
@patch("builtins.print")
def test_display(mock_print):
    fake_repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    fake_repo.list = []
    display(fake_repo)
    mock_print.assert_called_with("No items to display")


@patch("src.service.convert_list_of_objects_into_table", return_value="")
@patch("builtins.print")
def test_display(mock_print, mock_table):
    fake_repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    display(fake_repo)
    mock_print.assert_called_with("")


def test_add_product():
    item = Product("Coke", 1.1)
    repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    repo.add = MagicMock(return_value=1)
    actual = add(item, repo)
    expected = 1
    assert actual == expected


def test_update_product():
    item = Product("Coke", 1.1)
    repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    repo.add = MagicMock(return_value=1)
    index = 1
    updated_details = {"name": "Coke"}
    actual = update(index, updated_details, repo)
    expected = 1
    assert actual == expected


def test_delete():
    repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    repo.delete = MagicMock(return_value=1)
    index = 1
    actual = delete(index, repo)
    expected = 1
    assert actual == expected


def test_save():
    repo = ProductRepo(
        r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\test\resources\fake_product.csv")
    repo.save = MagicMock(return_value=1)

    actual = save(repo)
    expected = 1
    assert actual == expected

# @patch("builtins.input", side_effect = [0])
# @patch("builtins.print")
# def test_get_valid_index_from_user(mock_print,mock_input,fake_product_service):
#     expected = 0
#     actual = fake_product_service.get_valid_index_from_user()
#     assert actual == expected
#     mock_print.assert_called_with("Select from 0 to 1")

# # @patch('src.entites.product.Product.object_to_list', return_value= [Product("Coke", 2.2)] )
# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# def test_display(mock_product_repo, mock_product):
#     fake_product_service = Service(fake_product_service,Product)
#     fake_product_service.display()
#     mock_product.assert_has_called([call(Product("Coke", 2.2))])
#     mock_product_repo.get.assert_called_with()


# @patch("builtins.print")
# @patch('src.entities.product.Product.object_to_list', return_value= [Product("Coke", 2.2)] )
# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# def test_display_when_database_is_empty(mock_product_repo, mock_product, mock_print):
#     mock_product_repo.get.return_value = []
#     fake_product_service = Service(mock_product_repo,Product)
#     fake_product_service.display()
#     mock_print.assert_called_with("No items to display")


# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# @patch("src.entities.product.Product.create_item_from_user_input", return_value = Product("Coke",2.2))
# def test_add(mock_create_item, mock_product_repo):
#     #Assemble 
#     fake_product_service = Service(mock_product_repo, Product)

#     #Act 
#     actual = fake_product_service.add()

#     #Assert 
#     mock_create_item.assert_called_once_with()
#     mock_product_repo.add.assert_called_with(mock_create_item.return_value)


# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# @patch("src.entities.product.Product.get_update_details", return_value = {"name": "Cheese"})
# def test_update(mock_get_update_details, mock_product_repo):
#     #Assemble 
#     fake_product_service = Service(mock_product_repo, Product)

#     #Act 
#     actual=fake_product_service.update(0)
#     expected = {"name": "Cheese"} 

#     #Assert 
#     assert actual == expected
#     mock_get_update_details.assert_called_once_with()
#     mock_product_repo.update.assert_called_with(0, mock_get_update_details.return_value)


# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# def test_delete( mock_product_repo):
#     #Assemble 
#     fake_product_service = Service(mock_product_repo, Product)

#     #Act 
#     actual=fake_product_service.delete(0)
#     expected = 0

#     #Assert 
#     assert actual == expected
#     mock_product_repo.delete.assert_called_with(0)


# @patch('src.repo_impl.csv_product_repo.ProductRepo', autospec=True )
# def test_save(mock_product_repo):
#     #Assemble 
#     fake_product_service = Service(mock_product_repo, Product)

#     #Act 
#     fake_product_service.save()

#     #Assert
#     mock_product_repo.save.assert_called_with()

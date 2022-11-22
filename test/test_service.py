import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.service import Service
from src.product.product import Product
from product.product_repo import ProductRepo
import pytest
from unittest.mock import patch, call 

@pytest.fixture()
def fake_product_service():
    fake_product_repo = ProductRepo("resources/fake_product.csv")
    fake_product_service = Service(fake_product_repo, Product)
    yield fake_product_service
    fake_product_service= Service(fake_product_repo, Product)


@patch("builtins.input", side_effect = [0])
@patch("builtins.print")
def test_get_valid_index_from_user(mock_print,mock_input,fake_product_service):
    expected = 0
    actual = fake_product_service.get_valid_index_from_user()
    assert actual == expected
    mock_print.assert_called_with("Select from 0 to 1")




@patch('src.product.product.Product.object_to_list', return_value = ["Coke", 2.2]  )
@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
def test_display(mock_product_repo, mock_object_to_list, fake_product_service):
    
    p1 = Product("Coke", 2.2)
    mock_product_repo.get.return_value = [p1]
    fake_product_service = Service(mock_product_repo, Product)

    fake_product_service.display()
    for product in mock_product_repo.get():
        mock_object_to_list.assert_called_with(product)
    mock_product_repo.get.assert_called_with()


@patch("builtins.print")
@patch('src.product.product.Product.object_to_list', return_value= [Product("Coke", 2.2)] )
@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
def test_display_when_database_is_empty(mock_product_repo, mock_product, mock_print):
    mock_product_repo.get.return_value = []
    fake_product_service = Service(mock_product_repo,Product)
    fake_product_service.display()
    mock_print.assert_called_with("No items to display")
 




@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
@patch("src.product.product.Product.create_item_from_user_input", return_value = Product("Coke",2.2))
def test_add(mock_create_item_from_user_input, mock_product_repo):
    #Assemble 
    fake_product_service = Service(mock_product_repo, Product)

    #Act 
    actual = fake_product_service.add()

    #Assert 
    mock_create_item_from_user_input.assert_called_once_with()
    mock_product_repo.add.assert_called_with(mock_create_item_from_user_input.return_value)

    
@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
@patch("src.product.product.Product.get_update_details", return_value = {"name": "Cheese"})
def test_update(mock_get_update_details, mock_product_repo):
    #Assemble 
    fake_product_service = Service(mock_product_repo, Product)
    
    #Act 
    actual=fake_product_service.update(0)
    expected = {"name": "Cheese"} 

    #Assert 
    assert actual == expected
    mock_get_update_details.assert_called_once_with()
    mock_product_repo.update.assert_called_with(0, mock_get_update_details.return_value)




@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
def test_delete( mock_product_repo):
    #Assemble 
    fake_product_service = Service(mock_product_repo, Product)
    
    #Act 
    actual=fake_product_service.delete(0)
    expected = 0

    #Assert 
    assert actual == expected
    mock_product_repo.delete.assert_called_with(0)


@patch('src.product.csv_product_repo.ProductRepo', autospec=True )
def test_save(mock_product_repo):
    #Assemble 
    fake_product_service = Service(mock_product_repo, Product)
    
    #Act 
    fake_product_service.save()

    #Assert
    mock_product_repo.save.assert_called_with()


    




    

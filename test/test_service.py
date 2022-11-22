import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from unittest import mock
from unittest.mock import call, patch

import pytest

from src.product.product import Product
from src.product.product_repository import ProductFileRepository
from src.service import Service


@pytest.fixture()
def product_service():
    product_repository = ProductFileRepository(r"C:\Users\NayanGurung\Generation\Mini_Project\test\resources\fake_product.csv")
    product_service = Service(product_repository, Product)
    yield product_service
    product_service = Service(product_repository, Product)


@patch("builtins.input", side_effect = [0])
@patch("builtins.print")
def test_get_valid_index_from_user(mock_print,mock_input,product_service):
    expected = 0
    actual = product_service.get_index(4)
    assert actual == expected
    mock_print.assert_called_with("Select from 0 to 3")






@patch('src.product.product_repository.ProductFileRepository', autospec=True )
def test_display(mock_product_repo, product_service):
    
    p1 = Product("Coke", 2.2)
    mock_product_repo.list= [p1]
    product_service = Service(mock_product_repo, Product)
    product_service.display()
    mock_product_repo.get.assert_called_with()


@patch("builtins.print")
@patch('src.product.product.Product.object_to_list', return_value= [Product("Coke", 2.2)] )
@patch('src.product.product_repository.ProductFileRepository', autospec=True )
def test_display_when_database_is_empty(mock_product_repo, mock_product, mock_print):
    mock_product_repo.get.return_value = []
    product_service = Service(mock_product_repo,Product)
    product_service.display()
    mock_print.assert_called_with("No items to display")
 




@patch('src.product.product_repository.ProductFileRepository', autospec=True )
@patch("src.product.product.Product.create_item_from_user_input", return_value = Product("Coke",2.2))
def test_add(mock_create_item_from_user_input, mock_product_repo):
    #Assemble 
    product_service = Service(mock_product_repo, Product)

    #Act 
    actual = product_service.add()

    #Assert 
    mock_create_item_from_user_input.assert_called_once_with()
    mock_product_repo.add.assert_called_with(mock_create_item_from_user_input.return_value)

#  def update(self,*args):
#         index = self.get_valid_index_from_user(len(self.repo.get()))
#         updated_details = self.item_type.get_update_details(*args)
#         self.repo.update(index, updated_details) 
#         return updated_details

@patch.object(Product, "get_update_details" ,return_value ={"name":"Coke"})
@patch.object(Service, "get_index", return_value = 1)
def test_update(mock_ervice_method, mock_product_method,product_service):
    #Assemble 
    actual= product_service.update()
    expected ={"name":"Coke"}
    actual == expected
   


@patch.object(Service, "get_index", return_value = 1)
def test_delete( mock_service_method, product_service):
    #Assemble 
    actual = product_service.delete()
    
    #Act 
    expected = 1

    #Assert 
    assert actual == expected



@patch('src.product.product_repository.ProductFileRepository', autospec=True )
def test_save(mock_product_repo):
    #Assemble 
    product_service = Service(mock_product_repo, Product)
    
    #Act 
    product_service.save()

    #Assert
    mock_product_repo.save.assert_called_with()


    




    

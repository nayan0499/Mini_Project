import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.product.product import Product
from unittest.mock import patch
import pytest 


def test_product_constructor():
    product = Product("coke", 2.2)
    assert product.name == "Coke"

def test_object_to_list(): 
    product = Product("coke", 2.2)
    actual = Product.object_to_list(product)
    expected = ["Coke", 2.2]
    assert actual == expected

def test_object_to_list_raise_typeError(): 
    product = ("coke", 2.2)
    with pytest.raises(TypeError):
        Product.object_to_list(product)


def test_dict_to_obj():
    product_dict = {"name": "Coke", "price": 2.2}
    actual =Product.dict_to_obj(product_dict)

    assert actual.name == "Coke"

def test_dict_to_obj_invalid_key():
    product_dict = {"names": "Coke", "price": 2.2}
    actual = Product.dict_to_obj(product_dict)
    expected = -1
    assert actual == expected

@patch("builtins.input", side_effect = ["coke", 33])
def test_create_item_from_user_input(mock_input):
    product = Product.create_item_from_user_input()
    assert product.name == "Coke"

@patch("builtins.input", side_effect = ["fanta", ""])
def test_get_update_details(mock_input): 
    actual= Product.get_update_details()
    expected = {"name": "Fanta"}
    assert actual == expected 

@patch("builtins.input", side_effect = ["fanta", "2.2"])
def test_create_item_from_user_input(mock_input):
    
    product = Product.create_item_from_user_input()
    assert product.name == "Fanta"
    assert product.price == 2.2

@patch("builtins.print")
@patch("builtins.input", side_effect = ["fanta", "ff", "fanta", "3.3"])
def test_create_item_from_user_input_value_error(mock_input, mock_print):
    product = Product.create_item_from_user_input()
    mock_print.assert_called_with("price must be a float")


@patch("src.product.product.Product.get_validated_update_details", return_value = {"name": "Fanta"})
@patch("builtins.input", side_effect = ["fanta", ""])
def test_get_update_details_with_name(mock_input,mock_get_validated_update_details ):
    #Act
    update_details = Product.get_update_details()
    expected = {"name": "Fanta"}
    assert update_details == expected
    mock_get_validated_update_details.assert_called_with({"name": "fanta"})

@patch("src.product.product.Product.get_validated_update_details", return_value = {"price": 2.2})
@patch("builtins.input", side_effect = ["", "2.2"])
def test_get_update_details_with_price(mock_input,mock_get_validated_update_details ):
    #Act
    update_details = Product.get_update_details()
    expected = {"price": 2.2}
    assert update_details == expected
    mock_get_validated_update_details.assert_called_with({"price": '2.2'})


@patch("builtins.print")
@patch("src.product.product.Product.get_validated_update_details", return_value = {"price": 2.2})
@patch("builtins.input", side_effect = ["", "ff", "", "2.2"])
def test_get_update_details_with_type_error(mock_input,mock_get_validated_update_details, mock_print):
    #Act
    update_details = Product.get_update_details()
    expected = {"price": 2.2}
    assert update_details == expected
    mock_get_validated_update_details.assert_called_with({"price": 'ff'})



def test_get_validated_update_details():
    #Assemble 
    product_details = {"name": "fanta"}
    #Act
    update_details = Product.get_validated_update_details(product_details)
    expected = {"name": "Fanta"}
    assert update_details == expected

def test_get_validated_update_details_with_invalid_name():
    #Assemble 
    product_details = {"name": "33"}
    #Act
    with pytest.raises(TypeError) as ex:
        Product.get_validated_update_details(product_details)
    assert str(ex.value) == "Invalid name- try again"
  

def test_get_validated_update_details_with_invalid_price():
    #Assemble 
    product_details = {"price": "23df"}
    #Act
    with pytest.raises(TypeError) as ex:
        Product.get_validated_update_details(product_details)
    assert str(ex.value) =="price must only contain numbers -try again"
    





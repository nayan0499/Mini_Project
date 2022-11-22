from src.product.product import Product
from unittest.mock import patch
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_product_constructor():
    product = Product("coke", 2.2)
    assert product.name == "Coke"
    assert product.price == 2.2


def test_product_constructor_invalid_name():
    with pytest.raises(TypeError) as ex:
        Product("42", 2.2)
    assert str(ex.value) == "Name must not be numeric"


def test_product_constructor_invalid_price():
    with pytest.raises(TypeError) as ex:
        Product("Coke", "jj")
    assert str(ex.value) == "Price must not contain letters"


def test_product_constructor_raise_value_error():
    with pytest.raises(ValueError) as ex:
        Product("Coke", "-2.3")
    assert str(ex.value) == "Price must be greater than 0"


# def test_object_to_list():
#     product = Product("coke", 2.2)
#     actual = Product.object_to_list(product)
#     expected = ["Coke", 2.2]
#     assert actual == expected

# def test_object_to_list_raise_typeError():
#     product = ("coke", 2.2)
#     with pytest.raises(TypeError):
#         Product.object_to_list(product)


def test_dict_to_obj():
    product_dict = {"name": "Coke", "price": 2.2}
    actual = Product.dict_to_obj(product_dict)

    assert actual.name == "Coke"


def test_dict_to_obj_invalid_key():
    product_dict = {"names": "Coke", "price": 2.2}
    actual = Product.dict_to_obj(product_dict)
    expected = -1
    assert actual == expected


@patch("builtins.input", side_effect=["coke", 33])
def test_create_product_from_user_input(mock_input):
    product = Product.create_product_from_user_input()
    assert product.name == "Coke"


@patch("builtins.input", side_effect=["fanta", "2.2"])
def test_create_product_from_user_input(mock_input):
    product = Product.create_product_from_user_input()
    assert product.name == "Fanta"
    assert product.price == 2.2


@patch("builtins.print")
@patch("builtins.input", side_effect=["fanta", "ff", "fanta", "3.3"])
def test_create_product_from_user_input_value_error(mock_input, mock_print):
    product = Product.create_product_from_user_input()
    mock_print.assert_called_with("price must be a float")


def test_get_validated_update_details():
    # Assemble
    product_details = {"name": "fanta"}
    # Act
    update_details = Product.get_validated_update_details(product_details)
    expected = {"name": "Fanta"}
    assert update_details == expected


def test_get_validated_update_details_with_invalid_name():
    # Assemble
    product_details = {"name": "33"}
    # Act
    with pytest.raises(TypeError) as ex:
        Product.get_validated_update_details(product_details)
    assert str(ex.value) == "Invalid name- try again"


def test_get_validated_update_details_with_invalid_price():
    # Assemble
    product_details = {"price": "23df"}
    # Act
    with pytest.raises(TypeError) as ex:
        Product.get_validated_update_details(product_details)
    assert str(ex.value) == "price must only contain numbers -try again"

from unittest.mock import patch
from mini_project.app import Product
import pytest
from pytest import raises


def test_constructor():
    product = Product("Coke", 2.2)
    assert product.name == "Coke"
    assert product.price == 2.2


def test_constructor_with_invalid_name():
    with raises(TypeError) as exc_info:
        product = Product("23", 2.2)
    assert str(exc_info.value) == "Name must not be numeric"


def test_constructor_with_invalid_price():
    with pytest.raises(TypeError) as exc_info:
        product = Product("Cheese", -1)
    assert str(exc_info.value) == "Price must be greater than 0"


@patch('builtins.print')
@patch('builtins.input', side_effect=["323", "23"])
def test_from_user_input_with_invalid_name(mock_inputs, mock_print):
    with pytest.raises(Exception) as exc_info:
        Product.from_user_input()
        assert str(exc_info.value) == "Name must not be numeric"


@patch('builtins.print')
@patch('builtins.input', side_effect=["323", "jj"])
def test_from_user_input_with_invalid_price(mock_inputs, mock_print):
    with pytest.raises(Exception) as exc_info:
        Product.from_user_input()
        assert str(exc_info.value) == "could not convert string to float: 'jj'"


@patch('builtins.input', side_effect=["Fanta", "2.3"])
def test_from_user_input(mock_inputs):
    product = Product.from_user_input()
    assert product.name == "Fanta"
    assert product.price == 2.3


@patch('builtins.print')
@patch('builtins.input', side_effect=["", "dd", "", "1.1"])
def test_update_details_invalid_price(mock_input, mock_print):
    # Arrange
    product = Product("Pepper", 3.2)

    # Act
    product.update_details()

    # Assert
    mock_print.assert_called_once_with(
        "Invalid input- Try again \n Name should not be numeric  \n Price can have numbers only")


@patch('builtins.print')
@patch('builtins.input', side_effect=["23", "cheese", ""])
def test_update_details_invalid_name(mock_input, mock_print):
    # Arrange
    product = Product("Pepper", 3.2)

    # Act
    product.update_details()

    # Assert
    mock_print.assert_called_once_with(
        "Invalid input- Try again \n Name should not be numeric  \n 1Price can have numbers only ")

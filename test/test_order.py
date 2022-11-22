from src.order.order import Order
from unittest.mock import patch
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_order_constructor():
    order = Order("Nayan Gurung", "3 lindsey gardens, TW14 8PB", "07450989860", "1", "sent", "1,2")
    assert order.customer_name == "Nayan Gurung"
    assert order.customer_phone == "07450989860"


def test_dict_to_obj():
    order_dict = {'customer_name': 'Kate Moss', 'customer_address': 'Highgate, London, N6',
                  'customer_phone': '02038721200', 'order': '2', 'status': 'preparing', 'items': '2'}
    actual = Order.dict_to_obj(order_dict)
    assert actual.customer_phone == '02038721200'


def test_dict_to_obj_invalid_key():
    order_dict = {'customer_names': 'Kate Moss', 'customer_address': 'Highgate, London, N6',
                  'customer_phone': '02038721200', 'order': '2', 'statuss': 'preparing', 'items': '2'}
    actual = Order.dict_to_obj(order_dict)
    expected = -1
    assert actual == expected


@patch("builtins.input", side_effect=["Kate Moss", 'Highgate, London, N6', '02038721200', '2', 'preparing', '2'])
def test_create_order_from_user_input(mock_input):
    order = Order.create_order_from_user_input()
    assert order.customer_name == "Kate Moss"


def test_get_validated_update_details_():
    # Assemble
    order_details = {'customer_names': 'Kate Moss', 'customer_address': 'Highgate, London, N6',
                     'customer_phone': '02038721200'}
    # Act
    update_details = Order.get_validated_update_details(order_details)
    expected = {'customer_names': 'Kate Moss', 'customer_address': 'Highgate, London, N6',
                'customer_phone': '02038721200'}
    assert update_details == expected


def test_get_validated_update_details_with_invalid_phone():
    # Assemble
    order_details = {'customer_names': 'Kate Moss', 'customer_address': 'Highgate, London, N6',
                     'customer_phone': 'fwefwef'}
    # Act
    with pytest.raises(TypeError) as ex:
        Order.get_validated_update_details(order_details)
    assert str(ex.value) == "Invalid phone number - try again"

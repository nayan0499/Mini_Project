from src.courier.courier import Courier
from unittest.mock import patch
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_courier_constructor():
    courier = Courier("John", "2423423423")
    assert courier.name == "John"
    assert courier.phone == "2423423423"


def test_courier_constructor_invalid_name():
    with pytest.raises(TypeError) as ex:
        Courier("42", "874579974")
    assert str(ex.value) == "Name must not be numeric"


def test_courier_constructor_invalid_phone():
    with pytest.raises(TypeError) as ex:
        Courier("John", "rwewe")
    assert str(ex.value) == "Phone must not contain letters"


def test_dict_to_obj():
    courier_dict = {"name": "Mary", "phone": "43454543"}
    actual = Courier.dict_to_obj(courier_dict)

    assert actual.name == "Mary"


def test_dict_to_obj_invalid_key():
    courier_dict = {"names": "Mary", "phone": "43454543"}
    actual = Courier.dict_to_obj(courier_dict)
    expected = -1
    assert actual == expected


@patch("builtins.input", side_effect=["Mary", "4345344352"])
def test_create_courier_from_user_input(mock_input):
    courier = Courier.create_courier_from_user_input()
    assert courier.name == "Mary"


@patch("builtins.print")
@patch("builtins.input", side_effect=["John", "ff", "John", "895394753"])
def test_create_product_from_user_input_value_error(mock_input, mock_print):
    courier = Courier.create_courier_from_user_input()
    assert courier.name == "John"
    assert courier.phone == "895394753"


def test_get_validated_update_details_():
    # Assemble
    courier_details = {"name": "John"}
    # Act
    update_details = Courier.get_validated_update_details(courier_details)
    expected = {"name": "John"}
    assert update_details == expected


def test_get_validated_update_details_with_invalid_name():
    # Assemble
    courier_details = {"name": "33"}
    # Act
    with pytest.raises(TypeError) as ex:
        Courier.get_validated_update_details(courier_details)
    assert str(ex.value) == "Invalid name - Try again"


def test_get_validated_update_details_with_invalid_phone():
    # Assemble
    courier_details = {"phone": "feef"}
    # Act
    with pytest.raises(TypeError) as ex:
        Courier.get_validated_update_details(courier_details)
    assert str(ex.value) == "Invalid phone number - Try again"

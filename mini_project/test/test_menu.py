
from unittest.mock import Mock, patch
from mini_project.app import Menu


def test_set_selected_option():
    # Arrange
    mock_selected_option = 1
    mock_menu = Menu("Mock", ["Save any changes & Exit", "View the product menu",
                     "View the courier menu", "View the order menu"])

    # Act
    actual = mock_menu.set_selected_option(mock_selected_option)
    expected = 1

    # Assert
    assert expected == actual


@patch("builtins.print")
def test_set_selected_option_with_invalid_input(mock_print):
    # Arrange
    mock_selected_option = 10
    mock_menu = Menu("Mock", ["Save any changes & Exit", "View the product menu",
                     "View the courier menu", "View the order menu"])
    expected = -1

    # Act
    actual = mock_menu.set_selected_option(mock_selected_option)

    # Asseet
    assert expected == actual
    mock_print.assert_called_with(
        f"Invalid option selected - Select from 0 to {mock_menu.num_of_options}")


@patch("builtins.print")
def test_set_selected_option_with_string_input(mock_print):
    # Arrange
    mock_selected_option = "r"
    mock_menu = Menu("Mock", ["Save any changes & Exit", "View the product menu",
                     "View the courier menu", "View the order menu"])
    expected = -1

    # Act
    actual = mock_menu.set_selected_option(mock_selected_option)

    # Asseet
    assert expected == actual
    mock_print.assert_called_with(
        f"Invalid option selected - Option must not contain letters. Select from 0 to {mock_menu.num_of_options}")

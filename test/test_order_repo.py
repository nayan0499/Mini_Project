from src.order.order import Order
from src.order.csv_order_repo import OrderRepo
import pytest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture()
def fake_order_repo():
    fake_order_repo = OrderRepo("resources/fake_order.csv")
    yield fake_order_repo

    order1 = Order("Hilary Duff", 'LA', '02038721200', '1', 'delivered', '2,4')
    order2 = Order("Miley Cyrus", '7 things, California', '02038721200', '4', 'preparing', '1,2')
    fake_order_repo.list = [order1, order2]
    fake_order_repo.save()


def test_add(fake_order_repo):
    p = Order("Kate Moss", 'Highgate, London, N6', '02038721200', '2', 'preparing', '2')
    fake_order_repo.add(p)
    assert fake_order_repo.list[-1].customer_name == "Kate Moss"


def test_update(fake_order_repo):
    mock_updated_order_details = {"customer_name": "Chad Michael Murray"}
    fake_order_repo.update(0, mock_updated_order_details)
    assert fake_order_repo.list[0].customer_name == "Chad Michael Murray"


def test_delete(fake_order_repo):
    fake_order_repo.delete(0)
    assert len(fake_order_repo.list) == 1


def test_get(fake_order_repo):
    orders = fake_order_repo.get()
    assert len(orders) == 2
    pass


def test_save(fake_order_repo):
    fake_order_repo.add(Order("Kate Moss", 'Highgate, London, N6', '02038721200', '2', 'preparing', '2'))
    fake_order_repo.save()
    assert len(fake_order_repo.list) == 3

from src.courier.courier import Courier
from src.courier.csv_courier_repo import CourierRepo
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture()
def fake_courier_repo():
    fake_courier_repo = CourierRepo("resources/fake_courier.csv")
    yield fake_courier_repo

    courier1 = Courier("Hilary Duff", '02038721200')
    courier2 = Courier("Miley Cyrus", '02038721200')
    fake_courier_repo.list = [courier1, courier2]
    fake_courier_repo.save()


def test_add(fake_courier_repo):
    p = Courier("Kate Moss", '02038721200')
    fake_courier_repo.add(p)
    assert fake_courier_repo.list[-1].name == "Kate Moss"


def test_update(fake_courier_repo):
    mock_updated_courier_details = {"name": "Chad Michael Murray"}
    fake_courier_repo.update(0, mock_updated_courier_details)
    assert fake_courier_repo.list[0].name == "Chad Michael Murray"


def test_delete(fake_courier_repo):
    fake_courier_repo.delete(0)
    assert len(fake_courier_repo.list) == 1


def test_get(fake_courier_repo):
    couriers = fake_courier_repo.get()
    assert len(couriers) == 2
    pass


def test_save(fake_courier_repo):
    fake_courier_repo.add(Courier("Kate Moss", '02038721200'))
    fake_courier_repo.save()
    assert len(fake_courier_repo.list) == 3

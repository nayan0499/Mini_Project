
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import pytest

from src.product.product import Product
from src.product.product_repository import ProductFileRepository


@pytest.fixture()
def product_repository():

    product_repository = ProductFileRepository(r"C:\Users\NayanGurung\Generation\Mini_Project\test\resources\fake_product.csv")
    yield product_repository
    
    product1 = Product("Coke", 2.2)
    product2 = Product("Fanta", 2.0)
    product_repository.list = [product1, product2]
    product_repository.save()



def test_add(product_repository):
    p = Product("cheese", 2)
    product_repository.add(p)
    assert product_repository.list[-1].name == "Cheese"

def test_update(product_repository):
    mock_updated_product_details = {"name": "Water"}
    product_repository.update(0, mock_updated_product_details)
    assert product_repository.list[0].name == "Water"


def test_delete(product_repository):
    product_repository.delete(0)
    assert len(product_repository.list) == 1

def test_get(product_repository):
    products = product_repository.get()
    assert len(products) == 2
    pass

def test_save(product_repository):
    product_repository.add(Product("Chocolate", 3.3))
    product_repository.save()
    assert len(product_repository.list) == 3





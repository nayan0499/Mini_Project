
import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.product.product import Product
from product.product_repo import ProductRepo



import pytest

@pytest.fixture()
def fake_product_repo():

    fake_product_repo = ProductRepo("resources/fake_product.csv")
    yield fake_product_repo
    
    product1 = Product("Coke", 2.2)
    product2 = Product("Fanta", 2.0)
    fake_product_repo.list = [product1, product2]
    fake_product_repo.save()



def test_add(fake_product_repo): 
    p = Product("cheese", 2)
    fake_product_repo.add(p)
    assert fake_product_repo.list[-1].name == "Cheese"

def test_update(fake_product_repo):
    mock_updated_product_details = {"name": "Water"}
    fake_product_repo.update(0, mock_updated_product_details)
    assert fake_product_repo.list[0].name == "Water"


def test_delete(fake_product_repo):
    fake_product_repo.delete(0)
    assert len(fake_product_repo.list) == 1

def test_get(fake_product_repo):
    products = fake_product_repo.get()
    assert len(products) == 2
    pass

def test_save(fake_product_repo):
    fake_product_repo.add(Product("Chocolate", 3.3))
    fake_product_repo.save()
    assert len(fake_product_repo.list) == 3





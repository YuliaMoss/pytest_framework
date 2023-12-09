import pytest
import random
from api_collections.dataclasses.notes_dataclass import fake
from constants import ROOT_PATH
from db.sqllight_pack.products_repo import ProductsRepo


@pytest.fixture()
def products_repo(env):
    return ProductsRepo(f"{ROOT_PATH}{env.db_param.path}")


@pytest.fixture()
def fake_product():
    data = {
        "product_id": fake.pyint(9, 999),
        "product_name": fake.catch_phrase(),
        "category": fake.word(),
        "brand": fake.company(),
        "price": fake.pyfloat(left_digits=5, right_digits=2, positive=True, min_value=500, max_value=99999),
        "quantity": fake.pyint(0, 999),
        "country_of_origin": fake.country()
    }
    return data


@pytest.fixture()
def fake_three_products():
    products = []
    for _ in range(3):
        product = (
            fake.pyint(9, 999),
            fake.catch_phrase(),
            fake.word(),
            fake.company(),
            fake.pyfloat(left_digits=5, right_digits=2, positive=True, min_value=500, max_value=99999),
            fake.pyint(0, 999),
            fake.country()
        )
        products.append(product)
    return products


@pytest.fixture()
def choose_exist_product():
    data = {
        "product_id": random.randint(1, 20)
    }
    return data


@pytest.fixture()
def choose_product():
    data = {
        "product_id": random.randint(19, 500)
    }
    return data


@pytest.fixture()
def duplicate_product():
    data = {
        "product_id": 1,
        "product_name": "Laptop ASUS XPS 15",
        "category": "Computers",
        "brand": "ASUS",
        "price": 1200.00,
        "quantity": 10,
        "country_of_origin": "Taiwan"
    }
    return data


@pytest.fixture
def product_with_missing_info():
    """
    Returns a dictionary representing a product with missing information (not all mandatory fields provided).
    """
    return {
        'product_id': fake.pyint(9, 999),
        'product_name': fake.catch_phrase()
        # Інші обов'язкові поля не заповнені
    }

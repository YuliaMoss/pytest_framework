"""1 -
Сворити БД sqlite
Створити в ній таблицю товарів (категорія товарів на ваш вибір) - мінімум 5 колонок
Описати для таблиці класс репо з методами (CRUD) - INSERT, SELECT, UPDATE, DELTE
Написати мінімум 7 тестів (5 позитивних, 2 негативних)"""
from sqlite3 import IntegrityError


def test_get_all_products(products_repo):
    db = products_repo
    all_prod = db.get_all()
    for prod in all_prod:
        assert prod


def test_add_product(products_repo, fake_product):
    db = products_repo
    db.insert_one(**fake_product)
    all_prod = db.get_all()
    for prod in all_prod:
        assert prod


def test_get_products_by_country(products_repo):
    db = products_repo
    all_prod = db.get_products_by_country()
    assert all_prod


def test_add_product_by_id(products_repo, fake_product):
    db = products_repo
    db.insert_one(**fake_product)
    prod = db.get_one_by_id(product_id=fake_product['product_id'])
    assert prod == tuple(fake_product.values())


def test_insert_three_products(products_repo, fake_three_products):
    db = products_repo
    fake_prod = [fake_prod for fake_prod in fake_three_products]
    db.insert_many(fake_prod)
    all_prod = db.get_all()
    for prod in all_prod:
        assert prod


def test_update_one(products_repo, choose_exist_product):
    db = products_repo
    prod = db.get_one_in_tuple_by_id(product_id=choose_exist_product['product_id'])
    initial_quantity = prod[5]
    new_quantity = initial_quantity + 5
    # Updating product quantity
    product_id = choose_exist_product['product_id']
    updated_product = db.update_quantity(product_id=product_id, new_quantity=new_quantity)
    # Fetching the updated product
    res = updated_product
    # Verifying if the quantity of the product has been updated correctly
    assert res[5] == new_quantity


def test_delete_one_product(products_repo, choose_product):
    db = products_repo
    product_id = choose_product['product_id']
    deletion_success = db.delete_one(product_id=product_id)
    res = db.get_one_by_id(product_id)
    assert res == deletion_success
    assert deletion_success is None, f"Product{product_id} is not exists after deletion"


def test_insert_duplicate_product(products_repo, duplicate_product):
    db = products_repo
    try:
        db.insert_one(**duplicate_product)
        assert False, "Expected IntegrityError but got no exception"
    except IntegrityError as error:
        assert str(error) == "UNIQUE constraint failed: PRODUCTS.ID", f"Unexpected error message: {str(error)}"


def test_insert_product_with_missing_info(products_repo, product_with_missing_info):
    """
    Attempt to insert a product with missing information and expect an IntegrityError.
    """
    db = products_repo
    try:
        db.insert_minimal_product(**product_with_missing_info)
        assert False, "Expected IntegrityError but got no exception"
    except IntegrityError as error:
        assert "NOT NULL constraint failed" in str(error), f"Unexpected error message: {str(error)}"

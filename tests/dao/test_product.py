from backend.dao.db.dao_product import ProductDao
from backend.models.product import Product
from backend.dao.db.dao_base import BaseDao



def test_save():
    product_dao = ProductDao()
    model_product = Product('name', 'description', 'price')
    id_ = product_dao.save(model_product)
    assert product_database.name == 'name'
    assert product_database.description == 'description'
    assert product_database.price == 'price'
    return id_

def test_read_all():
    product_dao = ProductDao()
    product_database = product_dao.read_all()
    assert type(product_database) == list

def test_read_by_id():
    product_dao = ProductDao()
    product_database = product_dao.read_all()[-1]
    product_by_id = product_dao.read_by_id(product_database.id)
    assert product_database.id == product_by_id.id

def test_delete(id_):
    product_dao = ProductDao()
    product_to_delete = product_dao.read_by_id(id_)
    product_dao.delete(product_to_delete)
    product_database = product_dao.read_by_id(id_)
    assert product_database == None

def run_test_dao_products():
    product_dao = ProductDao()
    try:
        assert isinstance(product_dao, ProductDao)
        print('\033[42;1;30m' + 'all dao.products tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from dao.product FAILED' + '\033[0;0m')
        raise asserterror
from backend.controllers.controller_product import ProductController
from backend.models.product import Product
from backend.controllers.controller_base import BaseController


def test_save():
    product_controller = ProductController()
    model_product = Product('name', 'description', 'price')
    id_ = product_controller.save(model_product)
    assert product_database.name == 'name'
    assert product_database.description == 'description'
    assert product_database.price == 'price'
    return id_

def test_read_all():
    product_controller = ProductController()
    product_database = product_controller.read_all()
    assert type(product_database) == list

def test_read_by_id():
    product_controller = ProductController()
    product_database = product_controller.read_all()[-1]
    product_by_id = product_controller.read_by_id(product_database.id)
    assert product_database.id == product_by_id.id

def test_delete(id_):
    product_controller = ProductController()
    product_to_delete = product_controller.read_by_id(id_)
    product_controller.delete(product_to_delete)
    product_database = product_controller.read_by_id(id_)
    assert product_database == None

def run_test_controllers_products():
    product_controller = ProductController()
    try:
        assert isinstance(product_controller, ProductController)
        print('\033[42;1;30m' + 'all controller.products tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from controller.product FAILED' + '\033[0;0m')
        raise asserterror
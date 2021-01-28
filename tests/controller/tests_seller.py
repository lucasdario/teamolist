from backend.controllers.controller_base import BaseController
from backend.controllers.controller_seller import SellerController
from backend.models.seller import Seller


def test_controller_instance():
    seller_controller = SellerController()
    assert isinstance(seller_controller, BaseController)
    assert isinstance(seller_controller, SellerController)

def test_controller_create():
    seller_controller = SellerController()
    seller_model = Seller('Test_Name', '1010101010', 'nananan@papappa.raa')
    id_ = seller_controller.create(seller_model)
    seller_db_by_controller = seller_controller.read_by_id(id_)
    assert seller_db_by_controller.name == 'Test_Name'
    assert seller_db_by_controller.phone == '1010101010'
    assert seller_db_by_controller.email == 'nananan@papappa.raa'
    return id_

def test_controller_read_all():
    seller_controller = SellerController()
    seller_db_by_controller = seller_controller.read_all()
    assert type(seller_db_by_controller) == list

def test_controller_read_by_id():
    seller_controller = SellerController()
    seller_db_by_controller = seller_controller.read_all()[-1]
    seller_by_id = seller_controller.read_by_id(seller_db_by_controller.id)
    assert seller_db_by_controller.id == seller_by_id.id

def test_controller_update(id_):
    seller_controller = SellerController()
    seller_to_update = seller_controller.read_by_id(id_)
    seller_to_update.name = 'Test_Name_Updated'
    seller_to_update.phone = '66666666666'
    seller_to_update.email = 'Test_Emai@l_Upda.ted'
    seller_controller.update(seller_to_update)
    seller_db_by_controller = seller_controller.read_by_id(id_)
    assert seller_db_by_controller.name == 'Test_Name_Updated'
    assert seller_db_by_controller.phone == '66666666666'
    assert seller_db_by_controller.email == 'Test_Emai@l_Upda.ted'

def test_controller_delete(id_):
    seller_controller = SellerController()
    seller_to_delete = seller_controller.read_by_id(id_)
    seller_controller.delete(seller_to_delete)
    seller_db_by_controller = seller_controller.read_by_id(id_)
    assert seller_db_by_controller == None


def run_test_controller_seller():
    try:
        test_controller_instance()
        id_ = test_controller_create()
        test_controller_read_all()
        test_controller_read_by_id()
        test_controller_update(id_)
        test_controller_delete(id_)
        print('\033[42;1;30m'+"all controller.seller tests PASSED"+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+"some test from controller.seller FAILED"+'\033[0;0m')
        raise asserterror

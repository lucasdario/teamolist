from backend.dao.db.dao_base import BaseDao
from backend.dao.db.dao_seller import SellerDao
from backend.models.seller import Seller


def test_dao_instance():
    seller_dao = SellerDao()
    assert isinstance(seller_dao, BaseDao)
    assert isinstance(seller_dao, SellerDao)

def test_dao_save():
    seller_dao = SellerDao()
    seller_model = Seller('Test_Name', '5555555555', 'email@olist.br')
    id_ = seller_dao.save(seller_model)
    seller_db = seller_dao.read_by_id(id_)
    assert seller_db.name == 'Test_Name'
    assert seller_db.phone == '5555555555'
    assert seller_db.email == 'email@olist.br'
    return id_

def test_dao_read_all():
    seller_dao = SellerDao()
    seller_db = seller_dao.read_all()
    assert type(seller_db) == list

def test_dao_read_by_id():
    seller_dao = SellerDao()
    seller_db = seller_dao.read_all()[-1]
    seller_by_id = seller_dao.read_by_id(seller_db.id)
    assert seller_db.id == seller_by_id.id

def test_dao_delete(id_):
    seller_dao = SellerDao()
    seller_to_delete = seller_dao.read_by_id(id_)
    seller_dao.delete(seller_to_delete)
    seller_db = seller_dao.read_by_id(id_)
    assert seller_db == None


def run_test_dao_seller():
    try:
        test_dao_instance()
        id_ = test_dao_save()
        test_dao_read_all()
        test_dao_read_by_id()
        test_dao_delete(id_)
        print('\033[42;1;30m'+"all dao.seller tests PASSED"+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+"some test from dao.seller FAILED"+'\033[0;0m')
        raise asserterror

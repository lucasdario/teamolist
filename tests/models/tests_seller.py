from backend.models.base_model import BaseModel
from backend.models.seller import Seller


def test_seller_instance():
    seller = Seller('Test_Name', 'Test_Phone', 'Test_Email')
    assert isinstance(seller, BaseModel)
    assert isinstance(seller, Seller)

def test_seller_contructor():
    seller = Seller('Test_Name', 'Test_Phone', 'Test_Email')
    assert seller.name == 'Test_Name'
    assert seller.phone == 'Test_Phone'
    assert seller.email == 'Test_Email'


def run_test_model_seller():
    try:
        test_seller_instance()
        test_seller_contructor()
        print('\033[42;1;30m'+'all model.seller tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from model.seller FAILED'+'\033[0;0m')
        raise asserterror

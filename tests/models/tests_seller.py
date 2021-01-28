from backend.models.base_model import BaseModel
from backend.models.seller import Seller

class TestSeller():
    def test_seller_instance(self):
        seller = Seller('Test_Name', '988227143', 'victor.hausen@olist.com')
        assert isinstance(seller, BaseModel)
        assert isinstance(seller, Seller)


    def test_seller_contructor(self):
        seller = Seller('Test_Name', '988227143', 'victor.hausen@olist.com')
        assert seller.name == 'Test_Name'
        assert seller.phone == '988227143'
        assert seller.email == 'victor.hausen@olist.com'

        try:
            Seller("aaa6", "3nrew9f8", "4093240j3rf4")
        except Exception as e:
            print("Teste Passou")
            print(e)
            


    def run_test_model_seller(self):
        try:
            self.test_seller_instance()
            self.test_seller_contructor()
            print('\033[42;1;30m'+'all model.seller tests PASSED'+'\033[0;0m')
        except AssertionError as asserterror:
            print('\033[41;1;37m'+'some test from model.seller FAILED'+'\033[0;0m')
            raise asserterror

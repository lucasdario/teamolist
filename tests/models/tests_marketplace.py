from backend.models.base_model import BaseModel
from backend.models.marketplace import Marketplace


def test_model_marketplace_instance():
    mkt = Marketplace('Casas Bahia', 'Eletrodometico e Celulares')
    assert isinstance(mkt, BaseModel)
    assert isinstance(mkt, Marketplace)


def test_model_marketplace_value():
    mkt2 = Marketplace('Americanas', 'Departamentos')
    assert mkt2.name == 'Americanas'
    assert mkt2.description == 'Departamentos'


def run_test_model_marketplace():
    try:
        test_model_marketplace_instance()
        test_model_marketplace_value()
        print('\033[42;1;30m'+'all model.marketplace tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from model.marketplace FAILED'+'\033[0;0m')
        raise asserterror

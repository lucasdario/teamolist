import re
from sqlalchemy.sql.type_api import STRINGTYPE
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
    assert type(mkt2) is STRINGTYPE, "Name and Description aren't strings: %r" % mkt2
    if not mkt2.name:
        raise ValueError("Empty name aren't valid")
    if len(mkt2.name) > 200:
        raise ValueError("Description higher than 200 characters")
    if len(mkt2.description) > 600:
        raise ValueError("Description higher than 600 characters")
    if re.search(r"^[a-zA-Z0-9]+$", mkt2.name):
        raise ValueError("No special characters alowed in name.")
    return mkt2.name, mkt2.description


def run_test_model_marketplace():
    try:
        test_model_marketplace_instance()
        test_model_marketplace_value()
        print('\033[42;1;30m'+'all model.marketplace tests PASSED'+'\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m'+'some test from model.marketplace FAILED'+'\033[0;0m')
        raise asserterror

from backend.models.base_model import BaseModel
from backend.models.log import Log

data = '25/01/2021 às 13:37:20 => Listed Marketplace'


def test_log_instance():
    model = BaseModel()
    assert model.__abstract__
    assert isinstance(model, BaseModel)


def test_log_constructor():
    log = Log(data)
    assert isinstance(log.data, str)
    assert log.data is data


def run_test_model_log():
    try:
        test_log_instance()
        test_log_constructor()

        print('\033[42;1;30m' + 'all model.log tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from model.log FAILED' + '\033[0;0m')
        raise asserterror

from backend.models.base_model import BaseModel
from backend.models.log import Log

data = 'Listed Marketplace'


def test_log_instance():
    model = BaseModel()
    assert model.__abstract__
    assert isinstance(model, BaseModel)


def test_log_constructor():
    log = Log(data)
    assert isinstance(log.data, str)
    assert data in log.data
    assert len(log.data) > len(data)
    assert 'às' in log.data


def test_log_constructor_with_empty_data_should_raise_exception():
    try:
        Log('')
        raise AssertionError('ValueError exception not raised!')
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert e.args == ('You cannot create an empty log.',)


def run_test_model_log():
    try:
        test_log_instance()
        test_log_constructor()
        test_log_constructor_with_empty_data_should_raise_exception()

        print('\033[42;1;30m' + 'all model.log tests PASSED' + '\033[0;0m')
    except AssertionError as asserterror:
        print('\033[41;1;37m' + 'some test from model.log FAILED' + '\033[0;0m')
        raise asserterror

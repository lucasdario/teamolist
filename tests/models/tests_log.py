from backend.models.base_model import BaseModel
from backend.models.log import Log

data = '25/01/2021 às 13:37:20 => Listed Marketplace'


class TestLog:
    def test_base(self):
        model = BaseModel()
        assert model.__abstract__
        assert isinstance(model, BaseModel)

    def test_data(self):
        log = Log(data)
        assert isinstance(log.data, str)
        assert log.data is data

    def run_log_tests(self):
        self.test_base()
        self.test_data()

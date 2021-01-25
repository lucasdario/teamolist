from backend.dao.db.dao_log import LogDao
from backend.models.log import Log


class LogController():
    def __init__(self):
        self.__dao = LogDao()

    def create(self, data: str)-> None:
        return self.__dao.create(data)

    def read_all(self)-> list:
        return self.__dao.read_all()

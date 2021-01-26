from backend.dao.db.dao_log import LogDao
from backend.models.log import Log
from datetime import datetime


class LogController():
    def __init__(self):
        self.__dao = LogDao()

    def create(self, data: str)-> int:
        date = datetime.now()
        content = date.strftime(f"%d/%m/%Y às %H:%M:%S => {data}")
        result = self.__dao.save(Log(content))
        return result

    def read_all(self)-> list:
        return self.__dao.read_all()

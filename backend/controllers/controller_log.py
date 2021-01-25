from backend.dao.db.dao_log import LogDao
from backend.models.log import Log
from datetime import datetime


class LogController():
    def __init__(self):
        self.__dao = LogDao()

    def create(self, data: str)-> None:
        date = datetime.now()
        content = date.strftime(f"%d/%m/%Y às %H:%M:%S => {data}")
        self.__dao.save(Log(content))

    def read_all(self)-> list:
        return self.__dao.read_all()

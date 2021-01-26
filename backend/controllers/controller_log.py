from backend.dao.db.dao_log import LogDao
from backend.models.log import Log


class LogController:
    def __init__(self):
        self.__dao = LogDao()

    def create(self, data: str) -> int:
        result = self.__dao.save(Log(data))
        return result

    def read_all(self) -> list:
        return self.__dao.read_all()

from backend.controllers.controller_log import LogController
from backend.dao.db.dao_base import BaseDao


class BaseController:
    def __init__(self, dao: BaseDao, model_name: str):
        self.__dao = dao
        self.__log = LogController()
        self.__model_name = model_name

    def create(self, model: object) -> None:
        result = self.__dao.save(model)
        self.__log.create(f"Created {self.__model_name}")
        return result

    def read_by_id(self, id: int) -> object:
        result = self.__dao.read_by_id(id)
        return result

    def read_all(self) -> list:
        result = self.__dao.read_all()
        self.__log.create(f"Listed {self.__model_name}")
        return result

    def delete(self, model: object) -> None:
        self.__dao.delete(model)
        self.__log.create(f"Deleted {self.__model_name}")

    def update(self, model: object) -> None:
        result = self.__dao.save(model)
        self.__log.create(f"Updated {self.__model_name}")
        return result

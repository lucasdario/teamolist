from backend.controllers.controller_log import LogController
from backend.dao.db.dao_base import BaseDao

class BaseController:
    def __init__(self, dao: BaseDao):
        self.__dao = dao
        self.__log = LogController()

    def create(self, model: object)-> None: 
        self.__dao.save(model)
        self.__log.save(f"Created {self.__dao.model_name}")

    def read_by_id(self,id:int)-> object:
        result = self.__dao.read_by_id(id)
        return result

    def read_all(self)-> list:
        result = self.__dao.read_all()
        self.__log.save(f"Listed {self.__dao.model_name}")
        return result

    def delete(self, id:int)-> None:
        self.__dao.delete(id)
        self.__log.save(f"Deleted {self.__dao.model_name}")

    def update(self, model: object)->None:
        self.__dao.save(model)
        self.__log.save(f"Updated {self.__dao.model_name}")
from backend.dao.db.session import Session
from backend.models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model: object) -> None:
        self.__type_model = type_model


    def save(self, model: BaseModel) -> Int:
        with Session() as session:
            session.add(model)
            session.commit()
            id_ = model.id
            return id_

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
            return result

    def read_by_id(self, id: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id=id).first()
            return result

    def delete(self, model: BaseModel) -> Int:
        with Session() as session:
            session.delete(model)
            session.commit()
            id_=model.id
            return id_

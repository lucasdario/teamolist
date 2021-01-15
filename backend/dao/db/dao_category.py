from backend.dao.db import Connection
from backend.models.category import Category
from backend.dao.db.dao_base import BaseDao


class CategoryDao(BaseDao):
    def __init__(self):
        self.model_name = "Category"

    def create(self, model:Category) -> list:
        query = f"""INSERT INTO categories 
                        (NAME, DESCRIPTION) 
                        VALUES 
                        ('{model.name}','{model.description}'); """
        super().execute(query)

    def read_by_id(self, id:int)-> Category:
        query = f"SELECT ID, NAME, DESCRIPTION FROM categories WHERE ID = {id};"
        result = super().read(query)[0]
        category = Category(result[1],result[2] ,result[0])
        return category

    def read_all(self)->list:
        query = f"SELECT ID, NAME, DESCRIPTION FROM categories;"
        result_list = super().read(query)
        categories = []
        for result in result_list:
            category = Category(result[1],result[2] ,result[0])
            categories.append(category)
        return categories

    def delete(self, id:int)->None:
        query = f"DELETE FROM categories WHERE ID = {id};"
        super().execute(query)

    def update(self, model:Category)->None:
        query = f"""UPDATE categories 
                            SET 
                                NAME = '{model.name}',
                                DESCRIPTION = '{model.description}' 
                            WHERE ID = {model.id};
                            """
        super().execute(query)

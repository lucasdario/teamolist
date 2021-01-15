from backend.dao.db import Connection
from backend.models.product import Product
from backend.dao.db.dao_base import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        self.model_name = "Product"

    def create(self, model:Product) -> list:
        query = f"""INSERT INTO products 
                        (NAME, DESCRIPTION, PRICE) 
                        VALUES 
                        ('{model.name}','{model.description}', '{model.price}'); """
        super().execute(query)

    def read_by_id(self, id:int)-> Product:
        query = f"SELECT ID, NAME, DESCRIPTION, PRICE FROM products WHERE ID = {id};"
        result = super().read(query)[0]
        product = Product(result[1],result[2] , float(result[3].strip('$').replace(',', '')), result[0])
        return product

    def read_all(self)->list:
        query = f"SELECT ID, NAME, DESCRIPTION, PRICE FROM products;"
        result_list = super().read(query)
        products = []
        for result in result_list:
            product = Product(result[1],result[2] , float(result[3].strip('$').replace(',', '')), result[0])
            products.append(product)
        return products

    def delete(self, id:int)->None:
        query = f"DELETE FROM products WHERE ID = {id};"
        super().execute(query)

    def update(self, model:Product)->None:
        query = f"""UPDATE products 
                            SET 
                                NAME = '{model.name}',
                                DESCRIPTION = '{model.description}', 
                                PRICE = '{model.price}' 
                            WHERE ID = {model.id};
                            """
        super().execute(query)

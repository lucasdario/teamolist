from backend.models.seller import Seller
from backend.dao.db.dao_base import BaseDao


class SellerDao(BaseDao):
    def __init__(self):
        self.model_name = "Seller"

    def create(self, model: Seller) -> None:
        query = f"""INSERT INTO Sellers
                    (NAME, PHONE, EMAIL)
                    VALUES
                    ('{model.name}', '{model.phone}', '{model.email}');"""
        super().execute(query)

    def read_by_id(self, id: int) -> Seller:
        query = f"SELECT ID, NAME, PHONE, EMAIL FROM Sellers WHERE ID = {id};"
        result = super().read(query)[0]
        seller = Seller(result[1], result[2], result[3], result[0])

        return seller

    def read_all(self) -> list:
        query = f"SELECT ID, NAME, PHONE, EMAIL FROM Sellers;"
        result_list = super().read(query)
        sellers = []
        for result in result_list:
            seller = Seller(result[1], result[2], result[3], result[0])
            sellers.append(seller)

        return sellers

    def update(self, model: Seller) -> None:
        query = f"""UPDATE Sellers
                    SET
                        NAME = '{model.name}',
                        PHONE = '{model.phone}',
                        EMAIL = '{model.email}'
                    WHERE ID = {model.id}; 
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM Sellers WHERE ID = {id};"
        super().execute(query)

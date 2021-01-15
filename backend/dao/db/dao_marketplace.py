from backend.models.marketplace import Marketplace
from backend.dao.db.dao_base import BaseDao


class MarketplaceDao(BaseDao):
    def __init__(self):
        self.model_name = "Marketplace"

    def create(self, model: Marketplace) -> None:
        query = f"""INSERT INTO marketplaces
                    (NAME, DESCRIPTION)
                    VALUES
                    ('{model.name}', '{model.description}');"""
        super().execute(query)

    def read_by_id(self, id: int) -> Marketplace:
        query = f"SELECT ID, NAME, DESCRIPTION FROM marketplaces WHERE ID = {id};"
        result = super().read(query)[0]
        marketplace = Marketplace(result[1], result[2], result[0])

        return marketplace

    def read_all(self) -> list:
        query = f"SELECT ID, NAME, DESCRIPTION FROM marketplaces;"
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            marketplace = Marketplace(result[1], result[2], result[0])
            marketplaces.append(marketplace)

        return marketplaces

    def update(self, model: Marketplace) -> None:
        query = f"""UPDATE marketplaces
                    SET
                        NAME = '{model.name}',
                        DESCRIPTION = '{model.description}'
                    WHERE ID = {model.id}; 
                """
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM marketplaces WHERE ID = {id};"
        super().execute(query)

from backend.models.product import Product
from backend.dao.db.dao_base import BaseDao


class ProductDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Product)
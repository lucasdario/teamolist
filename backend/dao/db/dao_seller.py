from backend.models.seller import Seller
from backend.dao.db.dao_base import BaseDao


class SellerDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Seller)

from backend.models.marketplace import Marketplace
from backend.dao.db.dao_base import BaseDao


class MarketplaceDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Marketplace)
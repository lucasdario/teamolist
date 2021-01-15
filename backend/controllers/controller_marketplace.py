from backend.controllers.controller_base import BaseController
from backend.dao.db.dao_marketplace import MarketplaceDao


class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)

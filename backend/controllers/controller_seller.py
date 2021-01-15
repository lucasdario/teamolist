from backend.controllers.controller_base import BaseController
from backend.dao.db.dao_seller import SellerDao


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)

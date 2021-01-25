from backend.controllers.controller_base import BaseController
from backend.dao.db.dao_product import ProductDao


class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        super().__init__(self.__dao, 'Product')

from backend.controllers.controller_base import BaseController
from backend.dao.db.dao_category import CategoryDao


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao, 'Category')

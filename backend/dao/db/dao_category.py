from backend.models.category import Category
from backend.dao.db.dao_base import BaseDao


class CategoryDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Category)
        

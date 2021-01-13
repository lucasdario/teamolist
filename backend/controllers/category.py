from backend.dao.db.dao_category import read_categories, write_category
from backend.controllers.log import create_log
from backend.models.category import Category
from backend.models.log import Log


def create_category(category: Category):
    write_category(category)
    log = Log('Created Category')
    create_log(log)


def list_categories() -> list:
    categories = read_categories()
    log = Log('Listed Categories')
    create_log(log)
    return categories

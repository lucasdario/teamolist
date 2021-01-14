from backend.dao.db.dao_category import read_categories, write_category, delete_category, update_category
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

def remove_category(id: int):
    delete_category(id)
    log = Log('Deleted Category')
    create_log(log)

def edit_category(id: int, name: str, description: str):
    category = Category(name, description, id)
    update_category(category)
    log = Log('Updated Category')
    create_log(log)

print(read_categories())
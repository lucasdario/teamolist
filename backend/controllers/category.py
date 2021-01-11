from backend.dao.db.dao_category import read_categories, write_category


def create_category(form_data: dict):
    write_category(form_data)


def list_categories() -> list:
    categories = read_categories()
    return categories

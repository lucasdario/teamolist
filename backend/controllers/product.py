from backend.dao.db.dao_product import read_products, write_product


def create_product(form_data: dict):
    write_product(form_data)


def list_products() -> list:
    products = read_products()
    return products

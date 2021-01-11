from backend.dao.txt.dao_product import read_products, write_product
from backend.controllers.log import create_log


def create_product(form_data: dict):
    write_product(form_data)


def list_products() -> list:
    products = read_products()
    return products

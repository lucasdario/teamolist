from backend.dao.db.dao_product import read_products, write_product, update_product, delete_product
from backend.controllers.log import create_log
from backend.models.product import Product
from backend.models.log import Log


def create_product(product: Product):
    write_product(product)
    log = Log('Created Product')
    create_log(log)


def list_products() -> list:
    products = read_products()
    log = Log('Listed Products')
    create_log(log)
    return products


def remove_product(id: int):
    delete_product(id)
    log = Log('Deleted Product')
    create_log(log)


def edit_product(id: int, name: str, description: str, price: float):
    product = Product(name, description, float(price.strip('$').replace(',', '')), id)
    update_product(product)
    log = Log('Updated Product')
    create_log(log)

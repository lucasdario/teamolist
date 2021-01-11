from backend.dao.txt.dao_seller import read_sellers, write_seller
from backend.controllers.log import create_log


def create_seller(form_data: dict):
    write_seller(form_data)


def list_sellers() -> list:
    sellers = read_sellers()
    return sellers

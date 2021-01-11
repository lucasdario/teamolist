from backend.dao.txt.dao_marketplace import read_marketplaces, write_marketplace
from backend.controllers.log import create_log


def create_marketplace(form_data: dict):
    write_marketplace(form_data)


def list_marketplaces() -> list:
    marketplaces = read_marketplaces()
    return marketplaces

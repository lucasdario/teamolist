from backend.dao.db.dao_marketplace import read_marketplaces, write_marketplace


def create_marketplace(form_data: dict):
    write_marketplace(form_data)


def list_marketplaces() -> list:
    marketplaces = read_marketplaces()
    return marketplaces

from backend.dao.db.dao_marketplace import read_marketplaces, write_marketplace, update_marketplace, delete_marketplace
from backend.models.marketplace import Marketplace
from backend.models.log import Log


def create_marketplace(marketplace: Marketplace):
    write_marketplace(marketplace)
    log = Log('Created Marketplace')


def list_marketplaces() -> list:
    marketplaces = read_marketplaces()
    log = Log('Listed Marketplaces')
    return marketplaces


def edit_marketplace(id: int, name: str, description: str) -> None:
    marketplace = Marketplace(name, description, id)
    update_marketplace(marketplace)
    log = Log('Updated Marketplace')


def remove_marketplace(id: int) -> None:
    delete_marketplace(id)
    log = Log('Deleted Marketplace')

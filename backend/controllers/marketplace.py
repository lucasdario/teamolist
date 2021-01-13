from backend.dao.db.dao_marketplace import read_marketplaces, write_marketplace
from backend.controllers.log import create_log
from backend.models.marketplace import Marketplace
from backend.models.log import Log


def create_marketplace(marketplace: Marketplace):
    write_marketplace(marketplace)
    log = Log('Created Marketplace')
    create_log(log)


def list_marketplaces() -> list:
    marketplaces = read_marketplaces()
    log = Log('Listed Marketplaces')
    create_log(log)
    return marketplaces

from backend.dao.db.dao_seller import read_sellers, write_seller
from backend.controllers.log import create_log
from backend.models.seller import Seller
from backend.models.log import Log


def create_seller(seller: Seller):
    write_seller(seller)
    log = Log('Created Seller')
    create_log(log)


def list_sellers() -> list:
    sellers = read_sellers()
    log = Log('Listed Seller')
    create_log(log)
    return sellers

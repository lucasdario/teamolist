from backend.dao.db.dao_seller import read_sellers, write_seller, update_seller, delete_seller
from backend.controllers.log import create_log
from backend.models.seller import Seller
from backend.models.log import Log


def create_seller(seller: Seller) -> None:
    write_seller(seller)
    log = Log('Created Seller')
    create_log(log)


def list_sellers() -> list:
    sellers = read_sellers()
    log = Log('Listed Seller')
    create_log(log)
    return sellers


def edit_seller(id: int, name: str, phone: str, email: str) -> None:
    seller = Seller(name, phone, email, id)
    update_seller(seller)
    log = Log('Updated Seller')
    create_log(log)


def remove_seller(id: int) -> None:
    delete_seller(id)
    log = Log('Deleted Seller')
    create_log(log)

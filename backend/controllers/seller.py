from backend.dao.db.dao_seller import read_sellers, write_seller


def create_seller(form_data: dict):
    write_seller(form_data)


def list_sellers() -> list:
    sellers = read_sellers()
    return sellers

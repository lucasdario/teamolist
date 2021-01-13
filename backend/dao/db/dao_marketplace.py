from backend.dao.db import conn, cursor
from backend.models.marketplace import Marketplace


def write_marketplace(marketplace: Marketplace):
    cursor.execute(f"insert into marketplaces (name, description) values ('{marketplace.name}', '{marketplace.description}');")
    conn.commit()


def read_marketplaces() -> list:
    cursor.execute(f'select * from marketplaces;')
    result = cursor.fetchall()
    marketplaces = []
    for item in result:
        marketplace = Marketplace(item[1], item[2], item[0])
        marketplaces.append(marketplace)
    return marketplaces

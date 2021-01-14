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


def update_marketplace(marketplace: Marketplace) -> None:
    cursor.execute(f"""
                    UPDATE marketplaces SET name='{marketplace.name}', 
                    description='{marketplace.description}'
                    WHERE marketplaces.id='{marketplace.id}'    
                    """)
    conn.commit()


def delete_marketplace(id: int) -> None:
    cursor.execute(f"DELETE FROM marketplaces WHERE marketplaces.id='{id}'")
    conn.commit()

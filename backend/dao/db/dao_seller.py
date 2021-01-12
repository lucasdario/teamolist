from backend.dao.db import cursor, conn
from backend.models.seller import Seller


def write_seller(seller: Seller):
    cursor.execute(f"insert into sellers (name, email, phone) values ('{seller.name}', '{seller.email}', '{seller.phone}');")
    conn.commit()


def read_sellers() -> list:
    cursor.execute(f'select * from sellers;')
    result = cursor.fetchall()
    sellers = []
    for item in result:
        seller = Seller(item[1], item[2], item[3], item[0])
        sellers.append(seller)
    return sellers

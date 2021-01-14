from backend.dao.db import Connection
from backend.models.seller import Seller


def write_seller(seller: Seller):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"insert into sellers (name, email, phone) values ('{seller.name}', '{seller.email}', '{seller.phone}');")
        connection.commit()

def read_sellers() -> list:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from sellers;')
        result = cursor.fetchall()
        sellers = []
        for item in result:
            seller = Seller(item[1], item[2], item[3], item[0])
            sellers.append(seller)
        return sellers

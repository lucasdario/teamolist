from backend.dao.db import cursor, conn
from backend.models.seller import Seller


def write_seller(seller: Seller):
    cursor.execute(
        f"insert into sellers (name, phone, email) values ('{seller.name}', '{seller.phone}', '{seller.email}');")
    conn.commit()


def read_sellers() -> list:
    cursor.execute(f'select * from sellers;')
    result = cursor.fetchall()
    sellers = []
    for item in result:
        seller = Seller(item[1], item[2], item[3], item[0])
        sellers.append(seller)
    return sellers


def update_seller(seller: Seller) -> None:
    cursor.execute(f"""
                    UPDATE sellers SET name='{seller.name}',
                    phone='{seller.phone}',
                    email='{seller.email}'
                    WHERE sellers.id={seller.id}
                    """)
    conn.commit()


def delete_seller(id: int) -> None:
    cursor.execute(f"DELETE FROM sellers WHERE sellers.id={id}")
    conn.commit()

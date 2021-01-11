from backend.controllers.log import create_log
from backend.dao.db import cursor, conn


def write_seller(form_data):
    name = form_data["nome"]
    email = form_data["email"]
    phone = form_data["telefone"]
    cursor.execute(f"insert into sellers (name, email, phone) values ('{name}', '{email}', '{phone}');")
    conn.commit()
    create_log('Created Seller')


def read_sellers() -> list:
    cursor.execute(f'select * from sellers;')
    result = cursor.fetchall()
    sellers = []
    for seller in result:
        sellers.append({'name': seller[1], 'email': seller[2], 'telefone': seller[3]})
    create_log('Listed Seller')
    return sellers

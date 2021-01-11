from backend.controllers.log import create_log
from backend.dao.db import cursor, conn


def write_product(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    price = form_data["preco"]
    cursor.execute(f"insert into products (name, description, price) values ('{name}', '{description}', '{price}');")
    conn.commit()
    create_log('Created Product')


def read_products() -> list:
    cursor.execute(f'select * from products;')
    result = cursor.fetchall()
    products = []
    for product in result:
        products.append(
            {'name': product[1], 'description': product[2], 'price': float(product[3].strip('$').replace(',', ''))})
    create_log('Listed Products')
    return products

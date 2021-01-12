from backend.dao.db import cursor, conn
from backend.models.product import Product


def write_product(product: Product):
    cursor.execute(f"insert into products (name, description, price) values ('{product.name}', '{product.description}', '{product.price}');")
    conn.commit()


def read_products() -> list:
    cursor.execute(f'select * from products;')
    result = cursor.fetchall()
    products = []
    for item in result:
        product = Product(item[1], item[2], float(item[3].strip('$').replace(',', '')), item[0])
        products.append(product)
    return products

from backend.dao.db import Connection
from backend.models.product import Product


def write_product(product: Product):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"insert into products (name, description, price) values ('{product.name}', '{product.description}', '{product.price}');")
        connection.commit()


def read_products() -> list:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from products;')
        result = cursor.fetchall()
        products = []
        for item in result:
            product = Product(item[1], item[2], float(item[3].strip('$').replace(',', '')), item[0])
            products.append(product)
        return products


def update_product(product: Product):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
                        UPDATE products SET name='{product.name}',description='{product.description}',
                        price='{product.price}'
                        WHERE products.id='{product.id}'
                        """)
        connection.commit()


def delete_product(id: int):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM products WHERE products.id = '{id}'")
        connection.commit()

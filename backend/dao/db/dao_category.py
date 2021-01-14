from backend.dao.db import Connection
from backend.models.category import Category


def write_category(category: Category):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"insert into categories (name, description) values ('{category.name}', '{category.description}');")
        connection.commit()


def read_categories() -> list:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from categories;')
        result = cursor.fetchall()
        categories = []
        for item in result:
            category = Category(item[1], item[2], item[0])
            categories.append(category)
        return categories


def update_category(category: Category):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
                        UPDATE categories SET name='{category.name}',description='{category.description}'
                        WHERE categories.id='{category.id}'
                        """)
        connection.commit()
        

def delete_category(id: int):
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM categories WHERE categories.id = '{id}'")
        connection.commit()

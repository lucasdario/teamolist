from backend.dao.db import conn, cursor
from backend.models.category import Category


def write_category(category: Category):
    cursor.execute(f"insert into categories (name, description) values ('{category.name}', '{category.description}');")
    conn.commit()


def read_categories() -> list:
    cursor.execute(f'select * from categories;')
    result = cursor.fetchall()
    categories = []
    for item in result:
        category = Category(item[1], item[2], item[0])
        categories.append(category)
    return categories

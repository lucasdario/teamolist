from backend.dao.db import conn, cursor
from backend.controllers.log import create_log


def write_category(form_data: dict):
    name = form_data['nome']
    description = form_data['descricao']
    cursor.execute(f"insert into categories (name, description) values ('{name}', '{description}');")
    conn.commit()
    create_log('Created Category')


def read_categories() -> list:
    cursor.execute(f'select * from categories;')
    result = cursor.fetchall()
    categories = []
    for category in result:
        categories.append({'name': category[1], 'description': category[2]})
    create_log('Listed Categories')
    return categories

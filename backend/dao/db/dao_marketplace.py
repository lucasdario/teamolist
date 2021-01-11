from backend.controllers.log import create_log
from backend.dao.db import conn, cursor


def write_marketplace(form_data):
    name = form_data["nome"]
    description = form_data["descricao"]
    cursor.execute(f"insert into marketplaces (name, description) values ('{name}', '{description}');")
    conn.commit()
    create_log('Created Marketplace')


def read_marketplaces() -> list:
    cursor.execute(f'select * from marketplaces;')
    result = cursor.fetchall()
    marketplaces = []
    for marketplace in result:
        marketplaces.append({'name': marketplace[1], 'description': marketplace[2]})
    create_log('Listed Marketplaces')
    return marketplaces

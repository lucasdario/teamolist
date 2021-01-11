import json
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('PG_HOST')
USER = os.getenv('PG_USER')
PASSWORD = os.getenv('PG_PASSWORD')
DATABASE = os.getenv('PG_DATABASE')

conn = psycopg2.connect(
    f'host={HOST} dbname={DATABASE} user={USER} password={PASSWORD}')
cursor = conn.cursor()


def _is_table_created(table: str) -> bool:
    cursor.execute(
        f"select exists(select * from information_schema.tables where table_name='{table}')")
    return cursor.fetchone()[0]


def _are_tables_created():
    tables = ['logs', 'marketplaces', 'sellers', 'products', 'categories']
    not_created = []
    for table in tables:
        if _is_table_created(table):
            continue
        not_created.append(table)
    return not_created


def _get_queries_from_json():
    with open('queries.json') as file:
        return json.loads(file.read())


def create_tables():
    not_created = _are_tables_created()
    if not_created:
        queries = _get_queries_from_json()
        for table in not_created:
            cursor.execute(queries[table])
            conn.commit()

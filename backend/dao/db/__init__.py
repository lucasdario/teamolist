import json
import os

import psycopg2
from dotenv import load_dotenv

class Connection:
    def __get_connection_string(self):
        load_dotenv()

        host = os.getenv('PG_HOST')
        user = os.getenv('PG_USER')
        password = os.getenv('PG_PASSWORD')
        dbname = os.getenv('PG_DATABASE')

        connection_string = f'host={host} user={user} password={password} dbname={dbname}'
        return connection_string


    def __enter__(self):
        self.__connection = psycopg2.connect(self.__get_connection_string())
        return self.__connection


    def __exit__(self, type, value, trace):
        self.__connection.close()


    def _is_table_created(self, table: str) -> bool:
        with Connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"select exists(select * from information_schema.tables where table_name='{table}')")
            return cursor.fetchone()[0]


    def _are_tables_created(self):
        tables = ['logs', 'marketplaces', 'sellers', 'products', 'categories']
        not_created = []
        for table in tables:
            if self._is_table_created(table):
                continue
            not_created.append(table)
        return not_created


    def _get_queries_from_json(self):
        with open('queries.json') as file:
            return json.loads(file.read())


    def create_tables(self):
        with Connection() as connection:
            not_created = self._are_tables_created()
            if not_created:
                cursor = connection.cursor()
                queries = self._get_queries_from_json()
                for table in not_created:
                    cursor.execute(queries[table])
                    connection.commit()

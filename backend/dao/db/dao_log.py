from datetime import datetime
from backend.dao.db import Connection
from backend.models.log import Log
from backend.dao.db.dao_base import BaseDao


class LogDao(BaseDao):
    def create(self, data: str) -> None:
        date = datetime.now()
        content = date.strftime(f"%d/%m/%Y às %H:%M:%S => {data}")
        query = f"INSERT INTO logs (data) VALUES ('{content}');"
        super().execute(query)

    def read_all(self)->list:
        query = f"SELECT * FROM logs ORDER BY id DESC;"
        result_list = super().read(query)
        log_list = []
        for item in result_list:
            log = Log(item[1], item[0])
            log_list.append(log)
        return log_list

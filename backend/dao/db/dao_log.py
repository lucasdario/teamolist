from datetime import datetime
from backend.dao.db import Connection
from backend.models.log import Log


def write_log(log: Log):
    with Connection() as connection:
        cursor = connection.cursor()
        date = datetime.now()
        content = date.strftime(f"%d/%m/%Y às %H:%M:%S => {log.data}")
        cursor.execute(f"insert into logs (data) values ('{content}');")
        connection.commit()

def read_logs() -> list:
    with Connection() as connection:
        cursor = connection.cursor()
        log_list = []
        cursor.execute("select * from logs;")
        result = cursor.fetchall()
        for item in result:
            log = Log(item[1], item[0])
            if 'Listed' in item[1]:
                data = {'data': log.data, 'type': 'list', 'id': log.id}
                log_list.append(data)
            elif 'Created' in item[1]:
                data = {'data': log.data, 'type': 'create', 'id': log.id}
                log_list.append(data)
            elif 'Deleted' in item[1]:
                data = {'data': log.data, 'type': 'delete', 'id': log.id}
                log_list.append(data)
            elif 'Updated' in item[1]:
                data = {'data': log.data, 'type': 'update', 'id': log.id}
                log_list.append(data)
        return log_list

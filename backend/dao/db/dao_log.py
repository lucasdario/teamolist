from datetime import datetime

from backend.dao.db import conn, cursor


def write_log(content: str):
    date = datetime.now()
    content = date.strftime(f"%d/%m/%Y às %H:%M:%S => {content}")
    cursor.execute(f"insert into logs (data) values ('{content}');")
    conn.commit()


def read_logs() -> list:
    log_list = []
    cursor.execute("select * from logs;")
    result = cursor.fetchall()
    for log in result:
        if 'Listed' in log[1]:
            data = {'data': log[1], 'type': 'list'}
            log_list.append(data)
        elif 'Created' in log[1]:
            data = {'data': log[1], 'type': 'create'}
            log_list.append(data)
    return log_list

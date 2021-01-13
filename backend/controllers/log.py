from backend.dao.db.dao_log import read_logs, write_log
from backend.models.log import Log


def create_log(log: Log):
    write_log(log)


def list_logs() -> list:
    logs = read_logs()
    return logs

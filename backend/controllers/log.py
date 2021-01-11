from backend.dao.db.dao_log import read_logs, write_log


def create_log(content: str):
    write_log(content)


def list_logs() -> list:
    logs = read_logs()
    return logs

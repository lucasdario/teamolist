from backend.models.log import Log
from backend.dao.db.dao_base import BaseDao


class LogDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Log)

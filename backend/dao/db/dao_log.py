from backend.dao.db.dao_base import BaseDao
from backend.models.base_model import BaseModel
from backend.models.log import Log


class LogDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Log)

    def save(self, model: BaseModel) -> int:
        if model.id:
            raise PermissionError('You cannot modify a Log.')
        return super().save(model)

    def delete(self, model: BaseModel) -> None:
        raise PermissionError('You cannot delete a Log.')

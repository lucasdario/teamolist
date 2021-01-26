from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from backend.models.base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'logs'
    data = Column(String(length=500), nullable=False)

    def __init__(self, data: str) -> None:
        self.data = data

    @validates('data')
    def validate_data(self, _, data):
        if not data:
            raise ValueError('You cannot create an empty log.')
        date = datetime.now()
        data = date.strftime(f"%d/%m/%Y às %H:%M:%S => {data}")
        return data

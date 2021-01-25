from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Log(BaseModel):
    __tablename__ = 'logs'
    data =  Column(String(length=500), nullable = False)

    def __init__(self, data: str) -> None:
        self.data = data

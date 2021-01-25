from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Category(BaseModel):
    __tablename__ = 'categories'
    name = Column(String(length=200))
    description = Column(String(length=400))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

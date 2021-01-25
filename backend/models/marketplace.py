from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Marketplace(BaseModel):
    __tablename__ = 'marketplaces'
    name = Column(String(length=200), nullable = False)
    description = Column(String(length=600))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

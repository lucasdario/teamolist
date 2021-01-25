from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(length=200), nullable = False)
    description = Column(String(length=500), nullable = False)
    price = Column(String, nullable = False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

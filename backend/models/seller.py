from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'
    name = Column(String(length=200), nullable = False)
    phone = Column(String(length=11), nullable = False)
    email = Column(String(length=200), nullable = False)

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        
from sqlalchemy import Column, String
from backend.models.base_model import BaseModel
from sqlalchemy.orm import validates
import re


class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(length=200), nullable=False)
    description = Column(String(length=500), nullable=False)
    price = Column(String, nullable=False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name should not be empty!')
        if len(name) > 200:
            raise ValueError('Name should be 200 chars or less!')
        if not re.match(r'^[a-zà-úA-ZÀ-Ú0-9 ]+$', name):
            raise ValueError('Invalid chars in name!')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError('Description should not be empty!')
        if len(description) > 500:
            raise ValueError('Description should be 500 chars or less!')
        return description

    @validates('price')
    def validate_price(self, key, price):
        if not price:
            raise ValueError('Price should not be empty or zero!')
        if price < 0:
            raise ValueError('Price should not be negative!')
        return price

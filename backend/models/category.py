from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from backend.models.base_model import BaseModel
import re

class Category(BaseModel):
    __tablename__ = 'categories'
    name = Column(String(length=200))
    description = Column(String(length=400))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name cannot be empty!')
        if len(name) > 200:
            raise ValueError('Name must be less than 200 characters!')
        if not re.match(r'^[a-zà-úA-ZÀ-Ú0-9 ]+$', name):
            raise ValueError('Invalid characteres in name!')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) > 400:
            raise ValueError('Description must be less than 400 characters!')
        return description
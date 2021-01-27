import re
from sqlalchemy.orm import validates
from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplaces'
    name = Column( String(length=200), nullable = False)
    description = Column( String(length=600))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates("name")
    def validate_name(self, key, name):
        if name == "":
            raise ValueError("Empty name aren't valid")
        if len(name) > 200:
            raise ValueError("Description higher than 200 characters")
        if not re.search(r"^[\W]+$", name):
            raise ValueError("Name should have only letters (aA).")
        return name

    @validates("description")
    def validate_description(self, key, description):
        if len(description) > 600:
            raise ValueError("Description higher than 600 characters")
        return description
import re
from sqlalchemy import Column, String
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'
    __name = Column("name", String(length=200), nullable = False)
    __phone = Column("phone", String(length=11), nullable = False)
    __email = Column("email", String(length=200), nullable = False)

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        # nomes não podem ser inteiros os floats
        # nomes não devem conter números
        # espaço pode ter
        # não começar com espaço nem terminar
        # não tenha quebra de linha
        # testar caracteres especiais
        try:
            
            assert len(name) > 0, "Nome não pode ser vazio"
            assert not re.search(r"[0-9]", name), "Não podem haver números no nome"
            assert not re.search(r" {2,}", name), "Não podem haver mais de um espaço seguido"
            assert not re.search(r"^ ", name), "Não podem haver espaço no inicio"
            assert not re.search(r" $", name), "Não podem haver espaço no final"
            assert not re.search(r"\n", name), "Não podem haver quebra de linha '\\n' "
            assert re.search(r"[\w ]", name), "Não podem haver caracteres especiais"
            self.__name = name

        except Exception as e:
            print(name)
            raise Exception('Invalid name.') from e
        

    @property
    def phone(self) -> str:
        # não pode ter letras
        # tem que ter só numeros
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        try:
            assert re.search(r"[\d]{,14}", phone), "Phone number is too large"
            assert not re.search(r"\D", phone), "Non numeric characters are not allowed."
            self.__phone = phone
        except Exception as e:
            print(phone)
            raise Exception('Invalid phone number.') from e
    @property
    def email(self) -> str:
        # tem que seguir o formato iwqjioed@alguma_coisa.uma_terceira_coisa
        return self.__email
    @email.setter
    def email(self, email: str):
        try:
            assert re.search(r".{,50}", email), "Email number is too large"
            assert re.search(r"^[\w\.]+?@[\w\.]+?\.[\w\.]+?$", email)
            self.__email = email
        except Exception as e:
            raise Exception('Invalid e-mail.') from e
        
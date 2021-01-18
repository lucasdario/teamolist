class Product():

    def __init__(self, name: str, description: str, price: float, id: int = None) -> None:

        self.__name = name
        self.__description = description
        self.__price = price
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price
    
    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self):
        self.__name = name

    @description.setter
    def description(self):
        self.__description = description

    @price.setter
    def price(self):
        self.__price = price

    @id.setter
    def id(self):
        self.__id = id
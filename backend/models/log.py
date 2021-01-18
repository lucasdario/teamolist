class Log():

    def __init__(self, data: str, id: int = None) -> None:

        self.__data = data
        self.__id = id

    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self):
        self.__data = data
    
    @property
    def id(self):
        return self.__id
        
    @id.setter
    def id(self):
        self.__id = id
class Marketplace:
    def __init__(self, name:str, description:str, id:int = None):
        self.id = id
        self.name = name
        self.description = description
class RandomFood:
    def __init__(self, id:int, uid:str, dish:str, description:str, ingredient:str, measurement:str):
        self.id:int = id
        self.uid:str = uid
        self.description:str = description
        self.ingredient:str = ingredient
        self.measurement:str = measurement
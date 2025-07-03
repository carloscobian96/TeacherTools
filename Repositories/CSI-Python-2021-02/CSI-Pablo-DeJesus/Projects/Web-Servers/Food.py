#assigning a class
class Food:
    def __init__(self, id:int, uid:str,dish:str,description:str,ingredient:str,measurement:str):
        self.id = id, 
        self.uid = uid
        self.dish = dish
        self.description = description
        self.ingredient = ingredient
        self.measurement = measurement
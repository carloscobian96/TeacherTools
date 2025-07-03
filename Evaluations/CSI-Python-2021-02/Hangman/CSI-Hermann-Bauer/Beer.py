#Class for beer request
class Beer:
    def __init__(self, id:str, uid:str, brand:str, name:str, style:str, hop:str, yeast:str, malts:str, ibu:str, alcohol:str, blg:str):
        self.id = id
        self.uid= uid
        self.brand = brand
        self.name = name
        self.style = style
        self.hop = hop
        self.yeast = yeast
        self.malts = malts
        self.ibu = ibu
        self.alcohol = alcohol
        self.blg = blg


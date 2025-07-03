#Create a class to import them to File Deserialization and RequestDeserialization
class Color:
    def __init__(self, id:int, uid:str, hex_value:str, color_name:str, hsl_value:int , hsla_value:int):
        self.id = id
        self.uid = uid
        self.hex_value = hex_value
        self.color_name = color_name
        self.hsl_value = hsl_value
        self.hsla_value = hsla_value
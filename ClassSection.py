class Student:
  def __init__(self, name:str):
    self.name=name

class ClassSection:
  def __init__(self, professor:str, course:str, section:str, students):
    self.professor:str = professor
    self.course:str = course
    self.section:str = section
    self.students = students
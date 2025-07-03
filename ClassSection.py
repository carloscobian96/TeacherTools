import json
from os import path
import os
from pathlib import Path
import shutil
import subprocess
import webbrowser
from difflib import SequenceMatcher

myPath = str(Path(__file__).parents[0])
repoPath = path.join(myPath, 'Repositories')
browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
repoPath = path.join(myPath,'Repositories')

class Student:
  def __init__(self, name:str):
    self.name=name

class ClassSection:
  def __init__(self, professor:str, course:str, section:str, students):
    self.professor:str = professor
    self.course:str = course
    self.section:str = section
    myStudents = []
    for student in students:
      myStudents.append(Student(**student))
    self.students = myStudents

  # ----====8====----
  # Web Browser Functions
  # ----====8====----

  # Open a web browser window with each student 
  def openSection(self):
    webbrowser.get(browser)
    for student in self.students:
      url = f"https://github.com/{student.name}"
      webbrowser.open(url,1) 

  # Open a webbrowser window with each student's modifications of a file. 
  def compareSection(self):
    webbrowser.get(browser)
    for student in self.students:
      url = f"https://github.com/{self.professor}/{self.course}/compare/main...{student.name}:main"
      webbrowser.open(url,1) 
      
  # Open each student's version of a class file.
  def openClassFile(self,filePath):
    webbrowser.get(browser)
    for student in self.students:
      url = f"https://raw.githubusercontent.com/{student.name}/{self.course}/main/{filePath}"
      webbrowser.open(url,1) 

  # Open each student's version of a file located in their personal repository.
  def openStudentFile(self,filePath):
    webbrowser.get(browser)
    for student in self.students:
      url = f"https://raw.githubusercontent.com/{student.name}/{student.name}/main/{filePath}"
      webbrowser.open(url,1) 

  # View the raw of a student's personal repository file.
  def openStudentMarkdown(self,filePath):
    webbrowser.get(browser)
    for student in self.students:
      url = f"https://github.com/{student.name}/{student.name}/blob/main/{filePath}"
      webbrowser.open(url,1) 


  # ----====8====----
  # Git Functions
  # ----====8====----

  def cloneClassRepo(self):
    sectionPath = path.join(repoPath, f"{self.course}-{self.section}")
    for student in self.students:
      projectPath =  path.join(sectionPath, student.name )
      try: 
        os.makedirs(projectPath)  
      except:
        print("Folder Exists")

      url = f"https://github.com/{student.name}/{self.course}"
      subprocess.run(f"git clone {url} {str(projectPath)}")

  # def deleteClassRepo(self):
  #   sectionPath = path.join(repoPath, f"{self.course}-{self.section}")
  #   os.removedirs(sectionPath)

  # ----====8====----
  # Correcting Tools
  # ----====8====----
  def createRubric(self,project):
    evaluationRubricPath = path.join(myPath, "Evaluations")
    classEvaluationRubricPath = path.join(evaluationRubricPath, f"{self.course}-{self.section}")
    projectPath =  path.join(classEvaluationRubricPath, project)
    for student in self.students:
      try:
        studentFilePath = path.join(str(projectPath), str(student.name))
        outputFilePath = path.join(studentFilePath, f"{project}-Rubric.md")
        try: 
          os.makedirs(studentFilePath)  
        except:
          print("Folder Exists")
        # Locate rubric
        rubricFolderPath = path.join(str(path.join(myPath, "Resources")),"Rubric")
        rubricFilePath = path.join(rubricFolderPath, f"{project}.md" )
        instructionPath =  path.join(path.join(path.join(path.join(path.join(myPath, "Courses"),self.course), "Projects"), project), f"{project}.md")
        studentSubmission =  path.join(path.join(path.join(path.join(path.join(myPath, "Repositories"), f"{self.course}-{self.section}"), student.name), "Projects"), project)
        studentSubmissionRubric =  path.join(path.join(path.join(path.join(path.join(path.join(myPath, "Repositories"), f"{self.course}-{self.section}"), student.name), "Projects"), project),f"{project}.py")
        # Create rubric file
        with open(outputFilePath, "w+") as output, open(rubricFilePath, 'r') as rubric, open(studentSubmissionRubric, 'r') as submission, open(instructionPath, 'r') as instructions:
          # Create header
          rubricHeader = f"# {project} Rubric: {student.name}"
          print(rubricHeader)
          output.write(f"{rubricHeader}\n\n")
          # Rubric
          for line in rubric:
              output.write(line)
          output.write(f"\n<br>\n\n")
          output.write(f"### Submitted Work: \n\n")
          output.write(f"```python\n\n\n")
          # Student Submission
          try:
            for line in submission:
              output.write(line)
          except:{}
          output.write(f"\n```\n\n")
          # Instructions
          output.write(f"\n\n\n# Instructions:\n\n")
          for line in instructions:
            output.write(line)
        for file_name in os.listdir(studentSubmission):
          # construct full file path
          source = path.join(studentSubmission, file_name)
          destination = path.join(studentFilePath,file_name)
          # copy only files
          if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)
      except Exception as e: print(e)

  # Calculate the percent similarity between 2 students in a section.
  def compareSimilarity(self, project):
    sectionPath = path.join(repoPath, f"{self.course}-{self.section}")
    studentPaths = []
    students = os.listdir(sectionPath)
    # Project file list
    for student in students:  
      studentPath = os.path.join(sectionPath , student)
      studentProjects = os.path.join(studentPath , "Projects")
      studentProject = os.path.join(studentProjects , project)
      studentFile = os.path.join(studentProject , f"{project}.py")
      studentPaths.append(studentFile)
      print(str(studentFile))
    # Similarity detection
    for student in range(len(students)):
      try:
        text1 = open(studentPaths[student]).read()
        for compareStudent in range(len(students)):
          try:
            if student != compareStudent:
              text2 = open(studentPaths[compareStudent]).read()
              m = SequenceMatcher(None, text1, text2)
              print(f"Similarity between {students[student]} and {students[compareStudent]}: {round(m.ratio()*100,2)}")
          except:
            print(f"Unable to compare: with {students[compareStudent]}")
      except Exception as e:
        print(str(e))
        print(f"Unable to compare: {students[student]}")
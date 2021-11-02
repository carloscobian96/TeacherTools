from os import path, makedirs
import webbrowser
from pathlib import Path
import urllib.request
import subprocess
import traceback
import json

browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def openSection(classSection):
    webbrowser.get(browser)
    for student in classSection['students']:
        url = f"https://github.com/{classSection['professor']}/{classSection['course']}/compare/main...{student['name']}:main"
        webbrowser.open(url,1) 

def openClassFile(classSection,filePath):
    webbrowser.get(browser)
    for student in classSection['students']:
        url = f"https://raw.githubusercontent.com/{student['name']}/{classSection['course']}/main/{filePath}"
        webbrowser.open(url,1) 

def cloneProject(classSection,project,fileName):
    sectionPath = path.join(str(Path(__file__).parents[0]), f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        try:
            studentFilePath = path.join(str(projectPathPath), str(student['name']))
            try:
                makedirs(studentFilePath)
            except:{}
            outputFilePath = path.join(studentFilePath, fileName)

            url = f"https://raw.githubusercontent.com/{student['name']}/{classSection['course']}/main/Projects/{project}/{fileName}"
            print(url)
            urllib.request.urlretrieve(url, outputFilePath)
        except:{}

def executeFile(classSection,project,fileName):
    sectionPath = path.join(str(Path(__file__).parents[0]), f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        studentFilePath = path.join(str(projectPathPath), str(student['name']))
        studentFileName = path.join(studentFilePath, fileName)
        outputFileName = path.join(studentFilePath, 'output.txt')
        with open(outputFileName, "w+") as output:
            try:
                print(f"Running: {studentFileName}")
                subprocess.call(["python", studentFileName], stdout=output)
            except Exception:
                traceback.print_exc(file=output)
                continue

def createRubric(classSection,project,fileName):
    sectionPath = path.join(str(Path(__file__).parents[0]), f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        try:
            studentFilePath = path.join(str(projectPathPath), str(student['name']))
            outputFilePath = path.join(studentFilePath, fileName)

            # Locate rubric
            rubricFolderPath = path.join(str(Path(__file__).parents[0]), "Rubric")
            rubricFilePath = path.join(rubricFolderPath, f"{project}.md" )
            
            # Create rubric file
            with open(outputFilePath, "w+") as output, open(rubricFilePath, 'r') as rubric:
                # Create header
                rubricHeader = f"# {project} Rubric: {student['name']} \n"
                print(rubricHeader)
                output.write(rubricHeader)
                # output.write("\n\n")
                # output.write("Submission for: ")

                for line in rubric:
                    output.write(line)
        except:{}


#  Main
# classSection = {
#     "professor":"CSI-Carlos-Cobian",
#     "course":"CSI-Python-2021",
#     "section":"02",
#     "students": [
#         {"name":"CSI-Hermann-Bauer"},
#         {"name":"CSI-Rafael-Bonilla"},
#         {"name":"CSI-Diego-Cedeno"},
#         {"name":"CSI-Pablo-DeJesus"},
#         {"name":"CSI-Diego-Gaud"},
#         {"name":"CSI-Nicolas-Giner"},
#         {"name":"CSI-Andres-Juncos"},
#         {"name":"CSI-Edan-Padilla"},
#         {"name":"CSI-Francisco-Ruiz"},
#         {"name":"CSI-Mario-Sanchez"}
#     ]
# }

classSection = {
    "professor":"CSI-Carlos-Cobian",
    "course":"CSI-Python-2021",
    "section":"03",
    "students": [
        {"name":"CSI-Francisco-Aponte"},
        {"name":"CSI-Fernando-Arias"},
        {"name":"CSI-Rolando-Baez"},
        {"name":"CSI-Nicolas-Barreras"},
        {"name":"CSI-Jose-Canto"},
        {"name":"CSI-Ricardo-Davila"},
        {"name":"CSI-Mauricio-Malatrasi"},
        {"name":"CSI-Carlos-Quinones"},
        {"name":"CSI-Ezequiel-Ramirez"},
        {"name":"CSI-Osvaldo-Rocafort"},
        {"name":"CSI-Andres-Rodriguez"},
        {"name":"CSI-Carlos-Xu"}
    ]
}

# classSection = {
#     "professor":"CSI-Carlos-Cobian",
#     "course":"CSI-Java-2021",
#     "section":"01", 
#     "students": [
#         {"name":"CSI-Julio-Borges"},
#         {"name":"CSI-Pedro-Irene"},
#         {"name":"CSI-George-Lopez"},
#         {"name":"CSI-Antonio-Negron"},
#         {"name":"CSI-Pedro-Ochoa"},
#         {"name":"CSI-Guillermo-Perez"},
#         {"name":"CSI-David-Quiros"},
#         {"name":"CSI-Mateo-Ruiz"}
#     ]
# }


# filePath="Modules/Module5/RockPaperScissors.py"
# openClassFile(classSection,filePath)

# openSection(classSection)

cloneProject(classSection,'Projectile-Motion','Projectile-Motion.py')
cloneProject(classSection,'Projectile-Motion','ExperimentalData.py')
cloneProject(classSection,'Projectile-Motion','Projectile-Motion.json')
cloneProject(classSection,'Projectile-Motion','ExperimentData.py') # Allowed
cloneProject(classSection,'Projectile-Motion','ExperimentDatas.json') # Allowed

createRubric(classSection,'Projectile-Motion','Projectile-Motion-Rubric.md')
executeFile(classSection,'Projectile-Motion','Projectile-Motion.py')
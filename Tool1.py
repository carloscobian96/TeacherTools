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
        url = f"https://github.com/{student['name']}"
        webbrowser.open(url,1) 

def compareSection(classSection):
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
            rubricFolderPath = path.join(str(path.join(str(Path(__file__).parents[0]), "Resources")),"Rubric")
            rubricFilePath = path.join(rubricFolderPath, f"{project}.md" )
            
            # Create rubric file
            with open(outputFilePath, "w+") as output, open(rubricFilePath, 'r') as rubric:
                # Create header
                rubricHeader = f"# {project} Rubric: {student['name']}"
                print(rubricHeader)
                output.write(f"{rubricHeader}\n\n")

                for line in rubric:
                    output.write(line)
        except:{}


myOutputPath = Path(__file__).parents[0]

classFile = path.join(myOutputPath, 'Python-2021.json')
python = json.load(open(classFile,))

classFile = path.join(myOutputPath, 'Java-2021.json')
java = json.load(open(classFile,))

classFile = path.join(myOutputPath, 'NovaTech-2021.json')
novaTech = json.load(open(classFile,))

# filePath="Modules/Module5/RockPaperScissors.py"
# openClassFile(classSection,filePath)

# compareSection(classSection)
openSection(novaTech[1])

# cloneProject(classSection,'Projectile-Motion','Projectile-Motion.py')
# cloneProject(classSection,'Projectile-Motion','ExperimentalData.py')
# cloneProject(classSection,'Projectile-Motion','Projectile-Motion.json')
# cloneProject(classSection,'Projectile-Motion','ExperimentData.py') # Allowed
# cloneProject(classSection,'Projectile-Motion','ExperimentDatas.json') # Allowed

# createRubric(classSection,'Projectile-Motion','Projectile-Motion-Rubric.md')
# executeFile(classSection,'Projectile-Motion','Projectile-Motion.py')
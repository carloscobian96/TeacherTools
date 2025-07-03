from os import path, makedirs
import os
import webbrowser
from pathlib import Path
import urllib.request
import subprocess
import traceback
import json
import subprocess

browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
myPath = str(Path(__file__).parents[0])
repoPath = path.join(myPath,'Repositories')

# ----====o====----
# Define Functions
# ----====o====----
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

def openStudentFile(classSection,filePath):
    webbrowser.get(browser)
    for student in classSection['students']:
        url = f"https://raw.githubusercontent.com/{student['name']}/{student['name']}/main/{filePath}"
        webbrowser.open(url,1) 

def openStudentMarkdown(classSection,filePath):
    webbrowser.get(browser)
    for student in classSection['students']:
        url = f"https://github.com/{student['name']}/{student['name']}/blob/main/{filePath}"
        webbrowser.open(url,1) 

def cloneProject(classSection,project,fileName):
    sectionPath = path.join(repoPath, f"{classSection['course']}-{classSection['section']}")
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

def cloneStudentFile(classSection,project,fileName):
    sectionPath = path.join(repoPath, f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        try:
            studentFilePath = path.join(str(projectPathPath), str(student['name']))
            try:
                makedirs(studentFilePath)
            except:{}
            outputFilePath = path.join(studentFilePath, fileName)

            url = f"https://raw.githubusercontent.com/{student['name']}/{student['name']}/main/{fileName}"
            print(url)
            urllib.request.urlretrieve(url, outputFilePath)
        except:{}

def executeFile(classSection,project,fileName):
    sectionPath = path.join(repoPath, f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        studentFilePath = path.join(str(projectPathPath), str(student['name']))
        try:
            makedirs(studentFilePath)
        except:{}
        studentFileName = path.join(studentFilePath, fileName)
        outputFileName = path.join(studentFilePath, 'output.txt')
        with open(outputFileName, "w+") as output:
            try:
                print(f"Running: {studentFileName}")
                subprocess.call(["python", studentFileName], stdout=output)
            except Exception:
                traceback.print_exc(file=output)
                continue

def createRubric(classSection,project):
    sectionPath = path.join(repoPath, f"{classSection['course']}-{classSection['section']}")
    projectPathPath =  path.join(sectionPath, project)
    for student in classSection['students']:
        try:
            studentFilePath = path.join(str(projectPathPath), str(student['name']))
            outputFilePath = path.join(studentFilePath, f"{project}-Rubric.md")

            # Locate rubric
            rubricFolderPath = path.join(str(path.join(myPath, "Resources")),"Rubric")
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


def cloneClassRepo(classSection):
    sectionPath = path.join(repoPath, f"{classSection['course']}-{classSection['section']}")
    for student in classSection['students']:
        projectPathPath =  path.join(sectionPath, student['name'] )
        try: 
            os.makedirs(projectPathPath)  
        except:
            print("Folder Exists")

        url = f"https://github.com/{student['name']}/{classSection['course']}"
        subprocess.run(["git", "clone", url, str(projectPathPath)])

# ----====o====----
# Load Sections
# ----====o====----
sectionPath = path.join(Path(__file__).parents[0], 'Sections')

classFile = path.join(sectionPath, 'Python-2021.json')
python = json.load(open(classFile,))
[x*x for x in range(10)]

classFile = path.join(sectionPath, 'Java-2021.json')
java = json.load(open(classFile,))

classFile = path.join(sectionPath, 'NovaTech-2021.json')
novaTech = json.load(open(classFile,))

classFile = path.join(sectionPath, 'TEMP.json')
single = json.load(open(classFile,))




# ----====o====----
# Configure Execution
# ----====o====----

selected = python[0]
cloneClassRepo(selected)

selected = python[1]
cloneClassRepo(selected)

selected = java[0]
cloneClassRepo(selected)

selected = novaTech[0]
cloneClassRepo(selected)

selected = novaTech[1]
cloneClassRepo(selected)


# openSection(selected)
# compareSection(selected)
# openClassFile(selected,"Modules/Module6/Module6.md")
# openStudentMarkdown(selected,"Fan-Page.md")

# cloneStudentFile(selected,"Fan-Page","Fan-Page.html")

# ----====8888====----
#  Projectile Motion
# ----====8888====----
# cloneProject(selected,'Projectile-Motion','Projectile-Motion.py')
# cloneProject(selected,'Projectile-Motion','ExperimentalData.py')
# cloneProject(selected,'Projectile-Motion','Projectile-Motion.json')
# cloneProject(selected,'Projectile-Motion','experimentaldata.py') # Not Allowed

# createRubric(selected,'Projectile-Motion')
# executeFile(selected,'Projectile-Motion','Projectile-Motion.py')

# ----====8888====----
#  Web-Servers
# ----====8888====----
# cloneProject(selected,'Web-Servers','FileDeserialization.py')
# cloneProject(selected,'Web-Servers','RequestDeserialization.py')

# createRubric(selected,'Web-Servers')
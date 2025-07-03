from os import path
from pathlib import Path
import json

from ClassSection import ClassSection

browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
myPath = str(Path(__file__).parents[0])
repoPath = path.join(myPath,'Repositories')

# ----====o====----
# Load Sections
# ----====o====----
sectionPath = path.join(Path(__file__).parents[0], 'Sections')

classFile = path.join(sectionPath, 'Python-2021.json')
pySection = [ClassSection(**section) for section in json.load(open(classFile,))]
    
classFile = path.join(sectionPath, 'Java-2021.json')
jSection=[ClassSection(**section) for section in json.load(open(classFile,))]

classFile = path.join(sectionPath, 'NovaTech-2021.json')
novaTech = [ClassSection(**section) for section in json.load(open(classFile,))]

classFile = path.join(sectionPath, 'TEMP.json')
single = json.load(open(classFile,))

# ----====o====----
# Configure Execution
# ----====o====----

# novaTech[0].openStudentMarkdown("Jugabilidad.md")
# novaTech[0].openStudentMarkdown("HTML-Recipe.md")
# novaTech[0].openStudentFile("Fan-Page.html")
# novaTech[0].openStudentMarkdown("Fan-Page.md")


# pySection[0].openSection()
# pySection[0].compareSection()
# pySection[0].openClassFile("Modules/Module6/Module6.md")


jSection[0].cloneClassRepo()

pySection[0].cloneClassRepo()
pySection[1].cloneClassRepo()

# Incomplete
# pySection[0].createRubric("Geometric-Functions")
# pySection[0].compareSimilarity("Geometric-Functions")

# Incomplete
# pySection[0].createRubric("Projectile-Motion")
# pySection[0].compareSimilarity("Projectile-Motion")
# pySection[1].createRubric("Projectile-Motion")
# pySection[1].compareSimilarity("Projectile-Motion")

# pySection[0].createRubric("Hangman")
# pySection[0].compareSimilarity("Hangman")
# pySection[1].createRubric("Hangman")
# pySection[1].compareSimilarity("Hangman")

# pySection[0].createRubric("Snake")
# pySection[0].compareSimilarity("Snake")
# pySection[1].createRubric("Snake")
# pySection[1].compareSimilarity("Snake")
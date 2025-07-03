import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome. options import Options

# Locate webdriver path
myPath = Path(_file_).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

# Prevent window from opening. Background Task
options = Options()
options.headless=True

# Construct webdriver (executable_Path is now deprecated)
driver = webdriver.Chrome(executable_Path = driverPath, )

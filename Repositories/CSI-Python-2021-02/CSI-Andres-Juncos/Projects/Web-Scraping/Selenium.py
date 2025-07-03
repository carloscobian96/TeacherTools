from gettext import install


import os
from pathlib import Path
#import selenium
from selenium import webdriver

myPath = Path(__file__).parents[0]

geckodriverPath = f"{myPath}/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://google.com/")


import os
import json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()
# options.headless = True

driver = webdriver.Chrome(executable_path = driverPath, options = options)

driver.get = ("https://mangasee123.com/manga/Hajime-No-Ippo")

Chapters = driver.find_element(By.CLASS_NAME, '').text
print(Chapters)
driver.close()










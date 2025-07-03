import os 
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Locate webdriver path.
myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

#Prevent window from opening. Background Task
options = Options()
#options.headless=True

#Construct webdriver (executable_path is now deprecated)
driver = webdriver.Chrome(executable_path= driverPath, options = options)

#Open URL
driver.get("https://bakerskateboards.com/collections/all-boards/products/t-funk-crop-circles-deck-8-5")

#Find and print price element value. 

productTitle = driver.find_element(By.CLASS_NAME, 'ProductMeta__Title Heading u-h2')
print(productTitle)
driver.close()
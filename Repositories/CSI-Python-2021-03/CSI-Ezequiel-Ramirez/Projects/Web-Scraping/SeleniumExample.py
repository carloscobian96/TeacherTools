import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()

driver = webdriver.Chrome(executable_path = driverPath, options = options)

#Everything above this is universal. Everything below is project-specific, but the idea remains the same.
driver.get("https://www.amazon.com/")

price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
print(price)
driver.close()

#Options: 
#JSON
#ExtractList
#Carry Out Action
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

driver.get("https://www.amazon.com/GAOMON-Support-Pressure-Sensitive-Shortcut/dp/B07YFG742J")

price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
print(price)
driver.close()

import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()
# options.headlesss=True

driver = webdriver.Chrome(executable_path = driverPath, options = options)

driver.get("https://www.amazon.com/Novelty-Floats-Perfect-Realistic-Designs/dp/B07QQW54QF/ref=sr_1_7?crid=3CQXTWXFJH9LF&keywords=poop&qid=1648654720&sprefix=poop%2Caps%2C134&sr=8-7")

cashmoney = driver.find_element(By.CLASS_NAME, 'a price whole').text 
print(cashmoney)
driver.close()
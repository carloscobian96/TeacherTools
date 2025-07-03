from fileinput import close
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 


myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()
# options.headless = True

driver = webdriver.Chrome(executable_path= driverPath, options = options )


driver.get("https://www.ebay.com/")
driver.maximize_window()
driver.switch_to.parent_frame()
searchbar = driver.find_element(By.ID, 'gh-ac-box')
searchbar.send_keys("whatever")
#print(price)
#driver.close()
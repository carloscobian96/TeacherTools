import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options




myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()

driver = webdriver.Chrome(executable_path=driverPath,options=options)

driver.get("https://www.youtube.com/watch?v=myjEoDypUD8")

comment = driver.find_element(By.XPATH,"//*[@id='dislike-button']").text

print(comment)

#driver.close()






"""

This code likes looks for the most liked comment on the will smith youtube video and displays them

"""


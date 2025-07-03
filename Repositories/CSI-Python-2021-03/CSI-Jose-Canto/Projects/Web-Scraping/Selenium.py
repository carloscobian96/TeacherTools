import os
from pathlib    import Path
from selenium   import webdriver
from selenium.webdriver.common.by   import By
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.chrome.options  import Options

# Locate webdriver path
myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver"

# Prevent window from opening. Back Task
options = Options()
# options.deadless=True

# Construct webdriver (executable_path is now desprecated)
driver = webdriver.Chrome(executable_path = driverPath, options = options)

# Open URL
driver.get("https://www.supermaxonline.com/guaynabo/hogar-salud-y-belleza/higiene-personal/303335/sensodyne-rapid-relief-mint-3-4-oz")

#Find and print price alement value
price = driver.find_elements(By.CLASS_NAME, "red").text
print(price)
driver.close()


import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Download driver executable and place it in your working directory.
# Make sure you use the correct version for your browser
# https://github.com/mozilla/geckodriver/releases
# https://chromedriver.chromium.org/downloads

# Locate webdriver path. 
myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver.exe"

options = Options()
# Prevents error codes
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Headless prevent window from opening. Runs as background Task
# options.headless=True

# Construct webdriver (executable_path is now deprecated)
driver = webdriver.Chrome(executable_path = driverPath, options = options) 

# # Open URL
# driver.get("https://www.amazon.com/GIGABYTE-WATERFORCE-GV-N3080AORUSX-WB-10GD-REV2-0/dp/B09DV9GHT9")

# # Find and print price element value.  
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# print(price)

# # Add to cart
# driver.find_element(By.ID, 'add-to-cart-button').click()

search="WATERFORCE 3080".replace(" ","+")
driver.get("https://www.amazon.com/s?k=3080")

# driver.find_element(By.NAME,'q').send_keys("Testing")
# driver.find_element(By.NAME,'q').send_keys(Keys.RETURN)

# stuff = driver.find_elements(By.TAG_NAME,"s-search-result")
stuff = driver.find_elements(By.XPATH,"//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a")
for s in stuff:
    print(s.get_attribute("href"))

# //*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a
# print(stuff)




# Close Window
# driver.close()
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver"

options = Options()

driver = webdriver.Chrome(executable_path = driverPath, options = options)

driver.get("https://www.bestbuy.com/site/hp-omen-gaming-desktop-amd-ryzen-7-5800x-16gb-hyperx-memory-nvidia-geforce-rtx-3070-1tb-ssd-jet-black/6487502.p?skuId=6487502")

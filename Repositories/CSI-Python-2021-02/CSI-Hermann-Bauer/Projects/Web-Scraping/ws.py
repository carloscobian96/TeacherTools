from bs4 import BeautifulSoup
from selenium import webdriver
import bs4
driver =webdriver.Firefox(executable_path=r'/Users/hermannbauer/Downloads/geckodriver')

links = "https://www.plusportals.com/SanIgnacio"

driver.get(links)
email = driver.find_element_by_xpath("//*[@id=\"UserName\"]")
email.send_keys("22-106@sanignacio.pr")
password = driver.find_element_by_xpath("//*[@id=\"Password\"]")
password.send_keys("///")
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/input').click()

for i in range(7):
    j = i+1
    el = driver.find_elements_by_xpath(f'/html/body/div[4]/section/div/div[1]/section/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[{j}]/td[2]/a')
    print(el.get_attribute("textContent"))


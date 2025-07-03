from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\Users\carlo\Documents\CSI-Python-2021\chromedriver.exe")

for x in range(1,10000000000000000000000000000000):
    browser.get(
    "http://192.168.0.101/#/home/two")
  
# printing the content of entire page
print(browser.find_element_by_xpath("/html/body").text)
  
# closing the browser
browser.close()
import requests 
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977#.YmvsFpPMITU")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_ = "tombstone-container")
tonight = forecast_items[1]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
print(period)
temperature = tonight.find(class_="temp temp-low").get_text()
print(temperature)
description = tonight.find(class_="short-desc").get_text()
print(description)
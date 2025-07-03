from pydoc import describe
import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YmvsQNqZNPY")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
description = tonight.find(class_="short-desc").getText()
temperature = tonight.find(class_="temp temp-low").getText()
# print(tonight.prettiffy())
period = tonight.find(class_="period-name").getText()
print(period)
print(description)
print(temperature)
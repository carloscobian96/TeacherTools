import requests
import bs4

weather_site = requests.get("https://forecast.weather.gov/MapClick.php?lat=25.7492&lon=-80.2629")
weather_location = bs4.BeautifulSoup(weather_site.content, "html.parser")

elems = weather_location.find(id="seven-day-forecast")
forecast_items = elems.find_all(class_="tombstone-container")

tonight = forecast_items[1]

period = tonight.find(class_="period-name",).getText()
description = tonight.find(class_="short-desc").getText()
temperature = tonight.find(class_="temp temp-low").getText()

print(period)
print(description)
print(temperature)

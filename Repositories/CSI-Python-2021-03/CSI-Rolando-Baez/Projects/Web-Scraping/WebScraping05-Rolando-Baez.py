import bs4
import requests

website = requests.get("https://forecast.weather.gov/MapClick.php?textField1=31.8589&textField2=-106.4405#.YmvsYOjMJEY")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items=sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
# print(tonight.prettify())
period = tonight.find(class_='period-name').get_text()
print(period)
description = tonight.find(class_='short-desc').get_text()
print(description)
temp = tonight.find(class_='temp temp-low').get_text()
print(temp)
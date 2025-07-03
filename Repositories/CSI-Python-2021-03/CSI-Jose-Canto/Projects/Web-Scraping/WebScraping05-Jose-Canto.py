import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.35973000000007&lon=-66.11051999999995#.YmvtvPPMI_U")
forecast = bs4.BeautifulSoup(website.text, 'html.parser')
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items=sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[2]


period = tonight.find(class_="period-name").getText()
print(period)
shortDesc = tonight.find(class_="short-desc").getText()
print(shortDesc)
tempTemp = tonight.find(class_="temp temp-low").getText()
print(tempTemp)
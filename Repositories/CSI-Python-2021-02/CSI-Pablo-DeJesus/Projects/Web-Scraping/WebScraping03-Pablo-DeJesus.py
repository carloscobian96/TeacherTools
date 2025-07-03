import requests 
import bs4

website = requests.get("https://www.weather.gov/")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]

period = tonight.find(class_="period-name").getText()
print(period)
short_desc = tonight.find("class_"short-desc").getText()
print(short_desc)
temp_low = tonight.find(class_="temp temp-low").getText()
print(temp_low)
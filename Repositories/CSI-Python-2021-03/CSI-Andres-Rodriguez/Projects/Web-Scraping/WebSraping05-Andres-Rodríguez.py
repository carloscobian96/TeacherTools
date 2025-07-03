import requests
import bs4 

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.0117&lon=-66.6144#.YmvsAS1h1QI")
forecast = bs4.BeautifulSoup(website.content, "html.parser")

sevenDay = forecast.find(id= "seven-day-forecast")
forecast_items= sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
#print(tonight.prettify())

period = tonight.find(class_="period-name").getText()
print(period)
temperature = tonight.find(class_="temp temp-low").getText()
print(temperature)
short_description = tonight.find(class_="short-desc").getText()
print(short_description)
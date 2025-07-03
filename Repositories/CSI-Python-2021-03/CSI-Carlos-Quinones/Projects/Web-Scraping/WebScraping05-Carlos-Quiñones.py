import requests
import bs4


website = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Ymvr4trMK5c")

forecast = bs4.BeautifulSoup(website.content,'html.parser')

sevenDay= forecast.find(id="seven-day-forecast")

forecast_items = sevenDay.find_all(class_="tombstone-container")

tonigth = forecast_items[1]

period = tonigth.find(class_="period-name").get_text()


tempeture = tonigth.find(class_="temp temp-low").get_text()

description = tonigth.find(class_="short-desc").get_text()
print(period )
print(tempeture)
print(description)





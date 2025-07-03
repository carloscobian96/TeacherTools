import bs4
import requests

res = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.195230000000038&lon=-67.14017999999999#.Ymvr49pKg2w")

Forecast = bs4.BeautifulSoup(res.content, 'html.parser')
SevenDay = Forecast.find(id="seven-day-forecast")
Forecast_Items = SevenDay.find_all(class_="tombstone-container")
Tonight = Forecast_Items[2]
# print(Tonight.prettify())

Period = Tonight.find(class_="period-name").get_text()
print(Period)

Description = Tonight.find(class_="short-desc").get_text()
print(Description)

Temperature = Tonight.find(class_="temp temp-low").get_text()
print(Temperature)
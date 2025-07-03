import requests
import bs4 

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.394090000000062&lon=-66.14737999999994#.Yma69NNBzJ8")
forecast = bs4.BeautifulSoup(website.content,"html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_ = "tombstone-container")
tonight = forecast[1]

period = tonight.find(class_="period-name")
print(period)

aa = tonight.find(class_="short-desc")
print(aa)

ss = tonight.find(class_="temp-low")
print(ss)

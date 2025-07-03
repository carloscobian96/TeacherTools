import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?textField1=52.23&textField2=-174.22#.Yma6jZOZM1I")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
elems = forecast.select("p")

#print(len(elems))
print(elems[12].getText())
print(elems[14].getText())
print(elems[15].getText())

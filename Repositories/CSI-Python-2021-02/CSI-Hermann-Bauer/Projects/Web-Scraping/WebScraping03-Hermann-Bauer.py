import bs4
import requests

# res = requests.get("https://www.sanignacio.pr")
# SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')

# elems = SanIgnacioPR.select('link href')

# print(len(elems))
# print(str(elems))
# print(str(elems[0].getText()))

res = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.22260649800006&lon=-66.46895343099999#.Yma51dPMJQJ")
SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')

day = SanIgnacioPR.select("p.period-name")
desc = SanIgnacioPR.select("p.short-desc")
temp = SanIgnacioPR.select("p.temp.temp-low")


print(str(day[1].getText()))
print(str(desc[1].getText()))
print(str(temp[1].getText()))



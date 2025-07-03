import bs4
import requests 

res = requests.get("https://www.sanignacio.pr")
SanIgnacioPr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnacioPr.select('title')
print(len(elems))
print(str(elems))
print(elems[0].getText())
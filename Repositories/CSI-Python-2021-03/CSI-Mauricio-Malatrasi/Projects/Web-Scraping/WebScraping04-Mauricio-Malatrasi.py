import bs4
import requests

res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
SanIgnacioPR = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnacioPR.select("p")
print(elems[2].getText())
print(elems[3].getText())
print(elems[4].getText())
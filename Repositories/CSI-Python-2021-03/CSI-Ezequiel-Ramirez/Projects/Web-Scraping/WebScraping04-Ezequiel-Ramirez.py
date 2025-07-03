import bs4
import requests

res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
SanIgnacioPR = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnacioPR.select('p')
print(len(elems))
print(str(elems))
print(elems[0].getText())
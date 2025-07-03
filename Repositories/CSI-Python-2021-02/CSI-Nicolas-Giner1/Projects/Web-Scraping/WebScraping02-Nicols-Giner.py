import requests
import bs4
# res = requests.get("https://www.sanignacio.pr/")
# SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')
# elems = SanIgnacioPR.select('title')
# print(len(elems))
# print(str(elems))
# print(elems[0].getText)

res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio/")
SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')
elems = SanIgnacioPR.select('p')
print(len(elems))

print(elems[2].getText)
print(elems[3].getText)
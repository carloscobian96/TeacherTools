import bs4
import requests

# res = requests.get("https://www.sanignacio.pr")
# SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')

# elems = SanIgnacioPR.select('link href')

# print(len(elems))
# print(str(elems))
# print(str(elems[0].getText()))

res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
SanIgnacioPR = bs4.BeautifulSoup(res.content, 'html.parser')

elems = SanIgnacioPR.select('p')


print(str(elems[2].getText())+" "+str(elems[3].getText()))



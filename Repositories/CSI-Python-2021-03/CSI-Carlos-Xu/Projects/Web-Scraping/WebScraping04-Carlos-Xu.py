import requests
import bs4
res = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
Parrafos = bs4.BeautifulSoup(res.content, 'html.parser')
elems = Parrafos.select('p')

print(elems[2].getText())
print(elems[3].getText())
print(elems[4].getText())
# import webbrowser
# webbrowser.open("https://www.mangasee123.com/manga/Hajime-No-Ippo")
import requests 
res = requests.get("https://www.gutenberg.org/cache/epub/67783/pg67783.txt")
# print(len(res.text))
# print(res.text[:300])
playFile = open("Gaudentzia", "wb")
print(len(res.text))
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
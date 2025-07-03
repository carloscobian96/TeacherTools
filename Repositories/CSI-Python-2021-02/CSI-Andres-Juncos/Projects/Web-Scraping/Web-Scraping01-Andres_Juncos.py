# import webbrowser
# webbrowser.open("https://www.gutenberg.org/")
import requests
# res = requests.get("https://www.gutenberg.org/cache/epub/67775/pg67775.txt")
# print(len(res.text))
# print(res.text[:300])

res = requests.get("https://www.gutenberg.org/cache/epub/67789/pg67789.txt")
playFile = open("The Queen's Advocate","wb")
print(len(res.text))
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
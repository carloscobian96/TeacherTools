#import webbrowser
#webbrowser.open("https://espndeportes.espn.com/")
import requests 
#res = requests.get("https://gutenberg.org/cache/epub/67772/pg67772.txt")
#print(len(res.text))
#print(res.text[:300])
res = requests.get("https://gutenberg.org/cache/epub/67785/pg67785.txt")
playFile = open ("The Cat", "wb")
print(len(res.text))
for chunk in res.iter_content(276392):
    playFile.write(chunk)
playFile.close()
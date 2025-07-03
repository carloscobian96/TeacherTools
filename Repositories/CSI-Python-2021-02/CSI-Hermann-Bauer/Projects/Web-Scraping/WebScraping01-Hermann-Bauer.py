import chunk
import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67775/pg67775.txt")
playFile = open("Gaudenzia", "wb")
for char in res.iter_content(100001):
    playFile.write(char)
playFile.close

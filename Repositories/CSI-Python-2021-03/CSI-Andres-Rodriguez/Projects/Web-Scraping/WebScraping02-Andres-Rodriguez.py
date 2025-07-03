import requests
res = requests.get("https://www.gutenberg.org/cache/epub/20151/pg20151.txt")
playFile = open("Hidden Treasures.text", "wb")
for chunk in res.iter_content(1000000):
    playFile.write(chunk)
playFile.close()
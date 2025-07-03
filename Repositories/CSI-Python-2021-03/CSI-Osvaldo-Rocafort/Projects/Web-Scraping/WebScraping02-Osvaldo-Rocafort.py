import requests
res = requests.get("https://gutenberg.org/cache/epub/67889/pg67889.txt")
playFile = open("Un Vaincu.text","wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
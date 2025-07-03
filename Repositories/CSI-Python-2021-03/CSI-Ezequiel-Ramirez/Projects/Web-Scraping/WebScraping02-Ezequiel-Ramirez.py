import requests
res = requests.get("https://www.gutenberg.org/cache/epub/29086/pg29086.txt")
playFile = open("The Mushroom, Edible or Otherwise.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

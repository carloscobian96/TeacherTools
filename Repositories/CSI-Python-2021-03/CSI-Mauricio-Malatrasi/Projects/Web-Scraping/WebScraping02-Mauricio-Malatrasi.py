import requests
res = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
playFile = open("Othello.text", "wb" )
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
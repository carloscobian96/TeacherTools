import requests
res = requests.get("https://gutenberg.org/cache/epub/67893/pg67893.txt")
playFile = open("The Rover Boys Shipwrecked.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

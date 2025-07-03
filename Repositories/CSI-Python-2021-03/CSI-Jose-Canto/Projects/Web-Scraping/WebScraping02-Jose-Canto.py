import requests
res = requests.get("https://gutenberg.org/cache/epub/67893/pg67893.txt")
playfile = open("The Rover Boys Shipwrecked.text", "wb")
for chunck in res.iter_content(1000000):
    playfile.write(chunck)
playfile()
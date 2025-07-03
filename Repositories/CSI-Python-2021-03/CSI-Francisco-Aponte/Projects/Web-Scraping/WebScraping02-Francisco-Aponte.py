import requests
res = requests.get("https://gutenberg.org/cache/epub/67888/pg67888.txt")
playfile = open("Anticipation by Richard Tickell.text","wb" )
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile()
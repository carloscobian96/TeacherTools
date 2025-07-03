import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67891/pg67891.txt")
playFile = open("The Two Great Canyons, Excerpts From Letters Written on a Western Journey.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

import requests
res = requests.get ("https://gutenberg.org/cache/epub/67898/pg67898.txt")
res.raise_for_status()
playFile = open("The Bungalow Boys on the Great Lakes", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
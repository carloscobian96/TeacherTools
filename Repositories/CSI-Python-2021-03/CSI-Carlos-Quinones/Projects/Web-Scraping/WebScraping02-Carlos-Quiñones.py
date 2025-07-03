import requests

res = requests.get("https://www.gutenberg.org/files/2701/2701-0.txt")
playfile=open("Moby Dick.text","wb")

for chunk in res.iter_content(1276235):
    playfile.write(chunk)
playfile.close()

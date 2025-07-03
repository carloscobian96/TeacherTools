#import webbrowser
#webbrowser.open("https://www.newegg.com")
import requests
#res = requests.get("https://www.gutenberg.org/files/1661/1661-0.txt")
#print(len(res.text))
#print(res.text[:300])
res = requests.get("https://www.gutenberg.org/cache/epub/67781/pg67781.txt")
playFile = open("Bully Bull Frog and His Home in Rainbow Valley", "wb")
print(len(res.text))
for chunk in res.iter_content(151857):
    playFile.write(chunk)
playFile.close()
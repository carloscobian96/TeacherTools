# import webbrowser
# webbrowser.open("https://www.sanignacio.pr/")
import requests
# res = requests.get("https://www.gutenberg.org/cache/epub/67769/pg67769.txt")
# print(len(res.text))
# print(res.text[0:300]) 

res = requests.get("https://www.gutenberg.org/cache/epub/67789/pg67789.txt")

playFile = open("The Queen's Advocate", "wb")

print(len(res.text))

for chunk in res.iter_content(615730):
    playFile.write(chunk)
playFile.close()
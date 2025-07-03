# import webbrowser
# webbrowser.open("https://www.sanignacio.pr/")
import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67768/pg67768.txt")
print(len(res.text))
print(res.text[:300])
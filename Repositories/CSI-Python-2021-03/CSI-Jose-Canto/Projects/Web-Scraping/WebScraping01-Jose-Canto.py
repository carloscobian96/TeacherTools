import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(len(res.text))
print(res.text[:300])

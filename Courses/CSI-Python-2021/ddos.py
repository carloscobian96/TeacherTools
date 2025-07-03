import json, ssl
import urllib.request


addressURL = "http://192.168.0.101/protoapi/type"
addressURL = "http://192.168.0.101/protoapi/record"
addressURL = "http://192.168.0.101/protoapi/user"

for x in range(10000000):
    req = urllib.request.Request(addressURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # print(requestData)
    print(x)
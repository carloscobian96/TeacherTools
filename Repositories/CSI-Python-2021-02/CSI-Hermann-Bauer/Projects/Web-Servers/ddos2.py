

import json
import urllib

url = "http://192.168.0.101/protoapi/user"
r = urllib.request.urlopen(url)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
print(data)
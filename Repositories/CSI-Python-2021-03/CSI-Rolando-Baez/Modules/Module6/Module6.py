import json

favorite_album = {"Artist": "Aether Realm", "Album": "Tarot", "Release year": "2017", "Number of songs": "11"}

json_dump = json.dumps(favorite_album)

print(json_dump)
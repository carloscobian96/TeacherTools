import json

manga = {
    'Chainsaw Man': {
        'No. of Chapters': 91,
        'Genre': "Action-Horror Shonen",
        "Chapters I've Read": 78, 
    }
}


json_manga = json.dumps(manga, indent=4)

print(json_manga)

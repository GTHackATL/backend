import requests
import json

SECRET_KEY = 'AIzaSyBLlysxOu-B95J-2mCzAi8z1lA3SXPDO6U'

api_endpoint = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s" % SECRET_KEY

DEMO_DATA = {
    "request": {
        "passengers": {
            "adultCount": 1
        },
        "slice": [
            {
                "origin": "BOS",
                "destination": "LAX",
                "date": "2015-11-30"
            },
            {
                "origin": "LAX",
                "destination": "BOS",
                "date": "2015-12-05"
            }
        ]
    }
}

r = requests.post(api_endpoint, json=DEMO_DATA)

print(r.json())
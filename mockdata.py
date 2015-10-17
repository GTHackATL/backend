from itertools import permutations
import pprint
from geopy.distance import vincenty
from random import randint
from datetime import timedelta, datetime
from bson.json_util import dumps


pp = pprint.PrettyPrinter(indent=4)

dataset = {
    "cities": {
        "ATL": {
            "name": "Atlanta",
            "location": (33.7550, 84.3900)
        },
        "BOS": {
            "name": "Boston",
            "location": (42.3601, 71.0589)
        },
        "CHI": {
            "name": "Chicago",
            "location": (41.8369, 87.6847)
        },
        "PIT": {
            "name": "Pittsburgh",
            "location": (40.4397, 79.9764)
        }
    },
    "flights": [],
}

cities = dataset["cities"]
flights = dataset["flights"]

base_date = datetime.utcnow()


def get_price(distance):
    base_price = int(distance / 5)
    float_price = int(base_price / 3)
    return base_price + randint(-float_price, float_price)


# Generte random flight data with price based on location and random
for begin, end in permutations(cities, 2):
    for day in range(100):
        cur = {"origin": begin, "destination": end}
        cur["distance"] = vincenty(
            cities[begin]["location"], cities[end]["location"]).miles
        cur["date"] = base_date + timedelta(days=day)
        cur["price"] = get_price(cur["distance"])
        flights.append(cur)

print(dumps(dataset))

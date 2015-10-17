from itertools import permutations
import pprint
from geopy.distance import vincenty
from random import randint
from copy import deepcopy
from datetime import date, timedelta, datetime
from bson.json_util import dumps, loads

with open("mockdata.json", "r") as myfile:
    dataset = str(myfile.read())

dataset = loads(dataset)
base_date = datetime.utcnow()

flights = dataset["flights"]


def get_flight(origin, destination, days):
    desired_date = base_date.date() + timedelta(days=days)
    for flight in flights:
        if flight["origin"] == origin\
                and flight["destination"] == destination\
                and flight["date"].date() == desired_date:
            return flight


# (current_city, current_day, current_price)


class SequenceFinder:

    def __init__(self, start, min_day, max_total_day):
        self.min_day = min_day
        self.max_total_day = max_total_day
        self.start = start
        self.visited = {city: False for city in dataset["cities"]}
        self.visited[start] = True
        self.city_sequence = [(start, 0, 0)]
        self.initial_state = (start, 0, 0)
        self.min_price = 2 ** 30
        self.final_sequence = []

    def search(self, state):
        current_city, current_day, current_price = state
        unvisited = [
            city for city in self.visited if self.visited[city] == False]

        if not unvisited:  # no city left
            for days in range(current_day + self.min_day, self.max_total_day):
                flight = get_flight(current_city, self.start, days)
                final_price = current_price + flight["price"]
                self.city_sequence.append((self.start, days, final_price))
                if final_price < self.min_price:
                    self.min_price = final_price
                    self.final_sequence = deepcopy(self.city_sequence)
                self.city_sequence.pop()

        for city in unvisited:
            for days in range(current_day + self.min_day, self.max_total_day):
                flight = get_flight(current_city, city, days)
                next_state = (city, days, current_price + flight["price"])
                self.city_sequence.append(next_state)
                self.visited[city] = True
                self.search(next_state)
                self.visited[city] = False
                self.city_sequence.pop()

    def search_route(self):
        self.search(self.initial_state)
        return self.final_sequence

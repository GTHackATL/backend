from bottle import route, run
from route import SequenceFinder
import json


@route('/route/<city>/<min_day>/<max_total_day>')
def index(city, min_day, max_total_day):
    s = SequenceFinder(city, int(min_day), int(max_total_day))
    return json.dumps(s.search_route())
    # return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=5555)

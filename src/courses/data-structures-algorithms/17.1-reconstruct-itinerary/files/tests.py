import sys
import json
import heapq
from collections import defaultdict

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_find_itinerary(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)

    route = []
    stack = ["JFK"]
    while stack:
        while graph[stack[-1]]:
            stack.append(heapq.heappop(graph[stack[-1]]))
        route.append(stack.pop())
    return route[::-1]

inputs = [
    ([["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]],),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],),
    ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],),
    ([["JFK", "A"], ["A", "B"], ["B", "JFK"]],),
    ([["JFK", "B"], ["JFK", "A"], ["B", "JFK"]],),
    ([["JFK", "SFO"]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_itinerary(*i)
        assert main.find_itinerary(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def check(fn, *args):
    return fn(*args)

cases = [
    ('build_graph', (3, [[0, 1], [1, 2]])),
    ('build_graph', (1, [])),
    ('build_graph', (4, [[0, 1], [0, 2], [0, 3]])),
    ('build_graph', (4, [[2, 3], [0, 3], [1, 2]])),
    ('build_graph', (5, [[0, 1], [3, 4]])),
]

results = {}

for index, (name, args) in enumerate(cases):
    try:
        expected = check(globals()[name], *copy.deepcopy(args))
        assert check(getattr(main, name), *copy.deepcopy(args)) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

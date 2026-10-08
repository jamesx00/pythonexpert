import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

def check(cls, n, ops):
    uf = cls(n)
    out = []
    for op, a, b in ops:
        if op == "union":
            out.append(uf.union(a, b))
        else:
            out.append(uf.connected(a, b))
    return out

cases = [
    ('UnionFind', (3, [('union', 0, 1), ('connected', 0, 1), ('connected', 0, 2)])),
    ('UnionFind', (3, [('union', 0, 1), ('union', 1, 2), ('connected', 0, 2), ('union', 0, 2)])),
    ('UnionFind', (2, [('connected', 0, 1), ('union', 1, 0), ('connected', 1, 0)])),
    ('UnionFind', (6, [('union', 0, 1), ('union', 2, 3), ('union', 4, 5), ('connected', 1, 2), ('union', 1, 3), ('connected', 0, 2), ('connected', 0, 4)])),
    ('UnionFind', (4, [('union', 0, 0), ('union', 3, 2), ('union', 2, 3), ('connected', 3, 3)])),
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

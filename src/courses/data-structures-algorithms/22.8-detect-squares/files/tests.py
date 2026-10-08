import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

from collections import defaultdict


class ReferenceDetectSquares:
    def __init__(self):
        self.counts = defaultdict(int)
        self.points = defaultdict(set)

    def add(self, point):
        x, y = point
        self.counts[(x, y)] += 1
        self.points[x].add(y)

    def count(self, point):
        x, y = point
        total = 0
        for y2 in list(self.points[x]):
            if y2 == y:
                continue
            d = y2 - y
            for x2 in (x + d, x - d):
                total += self.counts[(x, y2)] * self.counts[(x2, y)] * self.counts[(x2, y2)]
        return total


def run(cls, operations):
    obj = cls()
    results = []
    for op, arg in operations:
        if op == 'add':
            obj.add(arg)
            results.append(None)
        else:
            results.append(obj.count(arg))
    return results


inputs = [
    [('add', [3, 10]), ('add', [11, 2]), ('add', [3, 2]), ('count', [11, 10])],
    [('add', [3, 10]), ('add', [11, 2]), ('add', [3, 2]), ('count', [14, 8])],
    [('add', [3, 10]), ('add', [11, 2]), ('add', [3, 2]), ('add', [11, 10]), ('count', [13, 6])],
    [('add', [0, 0]), ('add', [0, 2]), ('add', [2, 0]), ('add', [2, 2]), ('count', [0, 0])],
    [('add', [0, 0]), ('add', [0, 2]), ('add', [2, 0]), ('add', [2, 2]), ('add', [0, 0]), ('count', [0, 0])],
    [('count', [5, 5])],
]

results = {}

for index, ops in enumerate(inputs):
    try:
        expected = run(ReferenceDetectSquares, ops)
        actual = run(main.DetectSquares, ops)
        assert actual == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

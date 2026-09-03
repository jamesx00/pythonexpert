import sys
import json

from collections import OrderedDict
from unittest.mock import patch
patch('builtins.print').start()

import main

class ReferenceLRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def run_ops(cache, ops):
    output = []
    for op in ops:
        if op[0] == 'get':
            output.append(cache.get(op[1]))
        else:
            cache.put(op[1], op[2])
            output.append(None)
    return output

def test_lru_cache(capacity, ops):
    return run_ops(ReferenceLRUCache(capacity), ops)

inputs = [
    (2, [('put', 1, 10), ('put', 2, 20), ('get', 1), ('put', 3, 30), ('get', 2), ('get', 3)]),
    (1, [('put', 1, 1), ('get', 1), ('put', 2, 2), ('get', 1), ('get', 2)]),
    (2, [('put', 1, 1), ('put', 2, 2), ('put', 3, 3), ('get', 1), ('get', 3)]),
    (3, [('put', 1, 1), ('put', 2, 2), ('get', 1), ('put', 3, 3), ('put', 4, 4), ('get', 2), ('get', 1), ('get', 4)]),
    (2, [('get', 1), ('put', 1, 100), ('get', 1)]),
    (2, [('put', 1, 1), ('put', 1, 2), ('get', 1)]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_lru_cache(*i)
        student_cache = main.LRUCache(i[0])
        student_result = run_ops(student_cache, i[1])
        assert student_result == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

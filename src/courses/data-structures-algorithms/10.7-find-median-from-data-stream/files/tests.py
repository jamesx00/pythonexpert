import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(ops):
    data = []
    output = []
    for op, arg in ops:
        if op == 'add_num':
            data.append(arg)
            output.append(None)
        elif op == 'find_median':
            s = sorted(data)
            n = len(s)
            mid = n // 2
            if n % 2 == 0:
                output.append((s[mid - 1] + s[mid]) / 2)
            else:
                output.append(s[mid])
    return output

def run_main(ops):
    finder = main.MedianFinder()
    output = []
    for op, arg in ops:
        if op == 'add_num':
            finder.add_num(arg)
            output.append(None)
        elif op == 'find_median':
            output.append(finder.find_median())
    return output

inputs = [
    ([('add_num', 5), ('add_num', 1), ('find_median', None)],),
    ([('add_num', 5), ('add_num', 1), ('add_num', 3), ('find_median', None)],),
    ([('add_num', 2), ('find_median', None)],),
    ([('add_num', 6), ('add_num', 2), ('add_num', 9), ('add_num', 1), ('find_median', None)],),
    ([('add_num', -5), ('add_num', -2), ('add_num', -10), ('find_median', None)],),
    ([('add_num', 1), ('add_num', 1), ('add_num', 1), ('add_num', 1), ('find_median', None)],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_main(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

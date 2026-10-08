import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(ops):
    # ops is a list of (op_name, arg) tuples; arg is None for pop/top/get_min
    data = []
    output = []
    for op, arg in ops:
        if op == 'push':
            data.append(arg)
            output.append(None)
        elif op == 'pop':
            data.pop()
            output.append(None)
        elif op == 'top':
            output.append(data[-1])
        elif op == 'get_min':
            output.append(min(data))
    return output

def run_main(ops):
    stack = main.MinStack()
    output = []
    for op, arg in ops:
        if op == 'push':
            stack.push(arg)
            output.append(None)
        elif op == 'pop':
            stack.pop()
            output.append(None)
        elif op == 'top':
            output.append(stack.top())
        elif op == 'get_min':
            output.append(stack.get_min())
    return output

inputs = [
    ([('push', 5), ('push', 3), ('push', 7), ('get_min', None)],),
    ([('push', 5), ('push', 3), ('push', 7), ('pop', None), ('get_min', None)],),
    ([('push', 5), ('push', 3), ('push', 7), ('pop', None), ('pop', None), ('get_min', None)],),
    ([('push', -2), ('push', 0), ('push', -3), ('get_min', None), ('pop', None), ('top', None), ('get_min', None)],),
    ([('push', 1), ('push', 1), ('push', 1), ('get_min', None), ('pop', None), ('get_min', None), ('pop', None), ('get_min', None)],),
    ([('push', 4), ('top', None), ('get_min', None)],),
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

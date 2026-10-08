import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result

inputs = [
    (1,),
    (2,),
    (3,),
    (4,),
    (0,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_func(*i))
        assert sorted(main.generate_parentheses(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(temps):
    answer = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

inputs = [
    ([68, 70, 65, 72],),
    ([73, 74, 75, 71, 69, 72, 76, 73],),
    ([30, 40, 50, 60],),
    ([60, 50, 40, 30],),
    ([55],),
    ([50, 50, 50],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.daily_temperatures(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

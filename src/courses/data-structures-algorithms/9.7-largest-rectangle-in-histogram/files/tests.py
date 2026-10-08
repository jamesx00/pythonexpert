import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(heights):
    stack = []  # (start_index, height)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area

inputs = [
    ([2, 1, 5, 6, 2, 3],),
    ([2, 4],),
    ([1, 1, 1, 1],),
    ([6, 2, 5, 4, 5, 1, 6],),
    ([5],),
    ([0, 0, 0],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.largest_rectangle_area(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

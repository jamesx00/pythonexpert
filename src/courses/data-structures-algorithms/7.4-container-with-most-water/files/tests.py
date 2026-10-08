import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        best = max(best, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

inputs = [
    ([1, 7, 2, 5, 4, 7, 3],),
    ([1, 1],),
    ([4, 3, 2, 1, 4],),
    ([1, 2, 1],),
    ([0, 2],),
    ([2, 3, 4, 5, 18, 17, 6],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.max_area(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

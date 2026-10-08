import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(heights):
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water = 0
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
    return water

inputs = [
    ([0, 1, 0, 2, 1, 0, 3, 1, 0, 2],),
    ([4, 2, 3],),
    ([1, 1, 1],),
    ([5, 4, 1, 2],),
    ([],),
    ([3, 0, 0, 2, 0, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.trap_rain_water(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

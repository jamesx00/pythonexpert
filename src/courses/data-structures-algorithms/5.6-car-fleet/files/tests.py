import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(target, positions, speeds):
    cars = sorted(zip(positions, speeds), reverse=True)
    fleets = 0
    max_time = 0
    for pos, speed in cars:
        time = (target - pos) / speed
        if time > max_time:
            fleets += 1
            max_time = time
    return fleets

inputs = [
    (10, [0, 4], [2, 1]),
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
    (100, [0, 2, 4], [4, 2, 1]),
    (10, [3], [3]),
    (20, [0, 5, 10, 15], [1, 1, 1, 1]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.car_fleet(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

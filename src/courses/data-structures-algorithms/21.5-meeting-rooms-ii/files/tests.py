import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_min_meeting_rooms(intervals):
    if not intervals:
        return 0
    starts = sorted(iv[0] for iv in intervals)
    ends = sorted(iv[1] for iv in intervals)
    s_ptr = 0
    e_ptr = 0
    rooms = 0
    max_rooms = 0
    n = len(intervals)
    while s_ptr < n:
        if starts[s_ptr] < ends[e_ptr]:
            rooms += 1
            s_ptr += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1
            e_ptr += 1
    return max_rooms

inputs = [
    ([[0, 30], [5, 10], [15, 20]],),
    ([[7, 10], [2, 4]],),
    ([],),
    ([[1, 5]],),
    ([[1, 10], [2, 6], [3, 8], [4, 7]],),
    ([[1, 5], [5, 8], [2, 4]],),
    ([[1, 4], [2, 5], [7, 9], [8, 10]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_min_meeting_rooms(*i)
        assert main.min_meeting_rooms(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

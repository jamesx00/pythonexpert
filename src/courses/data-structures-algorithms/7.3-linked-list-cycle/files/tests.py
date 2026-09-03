import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def build_cycle_list(values, pos):
    if not values:
        return None
    nodes = [main.ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos is not None:
        nodes[-1].next = nodes[pos]
    return nodes[0]

def test_has_cycle(values, pos):
    return pos is not None

inputs = [
    ([3, 2, 0, -4], 1),
    ([1, 2], 0),
    ([1], None),
    ([], None),
    ([1, 2, 3, 4, 5], None),
    ([7, 8, 9], 2),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_has_cycle(*i)
        student_head = build_cycle_list(*i)
        assert main.has_cycle(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

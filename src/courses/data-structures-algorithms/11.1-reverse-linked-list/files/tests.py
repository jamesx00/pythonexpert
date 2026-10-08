import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_reverse_list(values):
    head = main.build_linked_list(values)
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return main.linked_list_to_list(prev)

inputs = [
    ([1, 2, 3, 4],),
    ([],),
    ([7],),
    ([1, 2],),
    ([5, 5, 5, 5],),
    ([9, -3, 4, 0, 2],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_reverse_list(*i)
        student_head = main.reverse_list(main.build_linked_list(*i))
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

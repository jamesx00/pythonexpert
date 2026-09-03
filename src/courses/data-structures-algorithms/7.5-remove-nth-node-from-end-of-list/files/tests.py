import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_remove_nth_from_end(values, n):
    head = main.build_linked_list(values)
    dummy = main.ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return main.linked_list_to_list(dummy.next)

inputs = [
    ([1, 2, 3, 4, 5], 2),
    ([1], 1),
    ([1, 2], 1),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5], 5),
    ([10, 20, 30, 40], 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_remove_nth_from_end(*i)
        student_head = main.remove_nth_from_end(main.build_linked_list(i[0]), i[1])
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

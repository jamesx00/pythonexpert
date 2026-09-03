import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_reorder_list(values):
    head = main.build_linked_list(values)
    if not head:
        return []

    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return main.linked_list_to_list(head)

inputs = [
    ([1, 2, 3, 4, 5],),
    ([1, 2, 3, 4],),
    ([1],),
    ([1, 2],),
    ([9, 8, 7],),
    ([1, 2, 3, 4, 5, 6],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_reorder_list(*i)
        student_head = main.build_linked_list(*i)
        main.reorder_list(student_head)
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

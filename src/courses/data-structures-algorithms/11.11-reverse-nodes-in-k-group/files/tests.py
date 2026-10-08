import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def test_reverse_k_group(values, k):
    head = main.build_linked_list(values)
    dummy = main.ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = group_next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return main.linked_list_to_list(dummy.next)

inputs = [
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 1),
    ([1, 2, 3, 4, 5, 6], 6),
    ([1, 2], 3),
    ([1, 2, 3, 4, 5, 6, 7], 3),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_reverse_k_group(*i)
        student_head = main.reverse_k_group(main.build_linked_list(i[0]), i[1])
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

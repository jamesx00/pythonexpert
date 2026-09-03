import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_merge_two_lists(values1, values2):
    l1 = main.build_linked_list(values1)
    l2 = main.build_linked_list(values2)
    dummy = main.ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return main.linked_list_to_list(dummy.next)

inputs = [
    ([1, 3, 5], [2, 4, 6]),
    ([], []),
    ([], [1, 2, 3]),
    ([5], [1]),
    ([1, 1, 3], [1, 2]),
    ([2, 8, 9], [1, 3, 4, 10]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_merge_two_lists(*i)
        student_head = main.merge_two_lists(main.build_linked_list(i[0]), main.build_linked_list(i[1]))
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

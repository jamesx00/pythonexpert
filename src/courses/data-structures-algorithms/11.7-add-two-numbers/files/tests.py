import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_add_two_numbers(values1, values2):
    l1 = main.build_linked_list(values1)
    l2 = main.build_linked_list(values2)
    dummy = main.ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = main.ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return main.linked_list_to_list(dummy.next)

inputs = [
    ([2, 4, 3], [5, 6, 4]),
    ([0], [0]),
    ([9, 9, 9], [1]),
    ([5], [5]),
    ([1, 2], [9, 9, 9]),
    ([9, 9], [9, 9]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_add_two_numbers(*i)
        student_head = main.add_two_numbers(main.build_linked_list(i[0]), main.build_linked_list(i[1]))
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_merge_k_lists(lists_of_values):
    heads = [main.build_linked_list(v) for v in lists_of_values]
    heap = []
    for i, node in enumerate(heads):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = main.ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return main.linked_list_to_list(dummy.next)

inputs = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]],),
    ([],),
    ([[]],),
    ([[5]],),
    ([[1, 2, 3], []],),
    ([[9], [1, 5], [2, 3, 7]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_merge_k_lists(*i)
        student_lists = [main.build_linked_list(v) for v in i[0]]
        student_head = main.merge_k_lists(student_lists)
        assert main.linked_list_to_list(student_head) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

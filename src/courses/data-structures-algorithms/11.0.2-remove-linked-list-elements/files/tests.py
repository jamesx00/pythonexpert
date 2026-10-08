import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def remove_elements(head, val):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

def check(fn, values, *rest):
    head = build_linked_list(values)
    return linked_list_to_list(fn(head, *rest))

cases = [
    ('remove_elements', ([1, 6, 2, 6, 3], 6)),
    ('remove_elements', ([7, 7, 7], 7)),
    ('remove_elements', ([], 1)),
    ('remove_elements', ([1, 2, 3], 4)),
    ('remove_elements', ([5, 1, 5, 5, 2, 5], 5)),
    ('remove_elements', ([1, 2, 2, 1], 2)),
]

results = {}

for index, (name, args) in enumerate(cases):
    try:
        expected = check(globals()[name], *copy.deepcopy(args))
        assert check(getattr(main, name), *copy.deepcopy(args)) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def check(fn, values, *rest):
    head = build_linked_list(values)
    return linked_list_to_list(fn(head, *rest))

cases = [
    ('middle_node', ([1, 2, 3, 4, 5],)),
    ('middle_node', ([1, 2, 3, 4],)),
    ('middle_node', ([1],)),
    ('middle_node', ([1, 2],)),
    ('middle_node', ([],)),
    ('middle_node', ([10, 20, 30, 40, 50, 60, 70],)),
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

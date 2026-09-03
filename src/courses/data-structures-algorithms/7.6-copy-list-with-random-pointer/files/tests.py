import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def build_random_list(values, randoms):
    if not values:
        return None
    nodes = [main.Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, r in enumerate(randoms):
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0]

def to_pairs(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    index = {id(n): i for i, n in enumerate(nodes)}
    pairs = []
    for n in nodes:
        r_index = index[id(n.random)] if n.random else None
        pairs.append((n.val, r_index))
    return pairs

def test_copy_random_list(values, randoms):
    head = build_random_list(values, randoms)
    if not head:
        return []

    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = main.Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return to_pairs(old_to_new[head])

inputs = [
    ([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]),
    ([1, 2], [1, 1]),
    ([3], [0]),
    ([], []),
    ([5, 6, 7], [None, None, None]),
    ([1, 2, 3, 4], [3, 2, 1, 0]),
]

results = {}

for index_i, i in enumerate(inputs):
    try:
        result = test_copy_random_list(*i)
        student_head = main.copy_random_list(build_random_list(*i))
        assert to_pairs(student_head) == result
        results[index_i + 1] = True
    except Exception:
        results[index_i + 1] = False

sys.stdout.write(json.dumps(results))

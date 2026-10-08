import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def _find(root, val):
    node = root
    while node is not None:
        if val == node.val:
            return node
        node = node.left if val < node.val else node.right
    return None

def test_lowest_common_ancestor(values, p_val, q_val):
    root = main.build_tree(values)
    p = _find(root, p_val)
    q = _find(root, q_val)

    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node.val

inputs = [
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5),
    ([2, 1], 2, 1),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 5),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_lowest_common_ancestor(*i)
        values, p_val, q_val = i
        root = main.build_tree(values)
        p = _find(root, p_val)
        q = _find(root, q_val)
        ancestor = main.lowest_common_ancestor(root, p, q)
        assert ancestor.val == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

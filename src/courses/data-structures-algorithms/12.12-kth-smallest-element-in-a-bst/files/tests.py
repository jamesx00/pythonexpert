import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_kth_smallest(values, k):
    root = main.build_tree(values)
    order = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        order.append(node.val)
        inorder(node.right)

    inorder(root)
    return order[k - 1]

inputs = [
    ([5, 3, 8, 2, 4, 7, 9], 3),
    ([5, 3, 8, 2, 4, 7, 9], 1),
    ([5, 3, 8, 2, 4, 7, 9], 7),
    ([3, 1, 4, None, 2], 1),
    ([3, 1, 4, None, 2], 4),
    ([1], 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_kth_smallest(*i)
        values, k = i
        root = main.build_tree(values)
        assert main.kth_smallest(root, k) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

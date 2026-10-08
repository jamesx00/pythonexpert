import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def _same(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and _same(a.left, b.left) and _same(a.right, b.right)

def test_is_subtree(root_values, sub_values):
    root = main.build_tree(root_values)
    sub_root = main.build_tree(sub_values)

    def helper(node):
        if node is None:
            return False
        if _same(node, sub_root):
            return True
        return helper(node.left) or helper(node.right)

    return helper(root)

inputs = [
    ([3, 4, 5, 1, 2], [4, 1, 2]),
    ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [2]),
    ([1, 2, 3], [4]),
    ([], [1]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_subtree(*i)
        root = main.build_tree(i[0])
        sub_root = main.build_tree(i[1])
        assert main.is_subtree(root, sub_root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

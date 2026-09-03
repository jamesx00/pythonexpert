import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_is_valid_bst(values):
    root = main.build_tree(values)

    def valid(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float('-inf'), float('inf'))

inputs = [
    ([5, 3, 8, 1, 4, 7, 9],),
    ([5, 1, 4, None, None, 3, 6],),
    ([2, 1, 3],),
    ([1, 1],),
    ([],),
    ([10, 5, 15, None, None, 6, 20],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_valid_bst(*i)
        root = main.build_tree(*i)
        assert main.is_valid_bst(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))

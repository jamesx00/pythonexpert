import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_is_balanced(values):
    root = main.build_tree(values)

    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1

inputs = [
    ([3, 9, 20, None, None, 15, 7],),
    ([1, 2, 2, 3, 3, None, None, 4, 4],),
    ([],),
    ([1],),
    ([1, 2, None, 3, None, 4],),
    ([1, 2, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_balanced(*i)
        root = main.build_tree(*i)
        assert main.is_balanced(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
